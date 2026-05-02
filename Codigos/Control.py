import sys
import numpy as np
import serial
from PyQt6 import QtWidgets, uic, QtCore
from PyQt6.QtWidgets import QTableWidgetItem
from PyQt6.QtCore import Qt


def DH(T, a, d, alp):
    return np.array([
        [np.cos(T), -np.cos(alp)*np.sin(T),  np.sin(alp)*np.sin(T), a*np.cos(T)],
        [np.sin(T),  np.cos(alp)*np.cos(T), -np.sin(alp)*np.cos(T), a*np.sin(T)],
        [0,          np.sin(alp),            np.cos(alp),           d],
        [0,          0,                      0,                     1]
    ])


def cinematica_directa(q):
    q = np.radians(q)
    q1, q2, q3, q4, q5, q6 = q
    L1=109.99; L2=104.99; L3=94.09
    L4=50.75; L5=28.74; L6=56.47
    T1=q1
    T2=q2
    T3=q3 + np.pi/2
    T4=q4
    T5=q5 + np.pi/2
    T6=q6
    d1=L1; d2=0; d3=0
    d4=L3+L4; d5=0; d6=L5+L6
    a1=0; a2=L2; a3=0
    a4=0; a5=0; a6=0
    alp1=np.pi/2; alp2=0; alp3=-np.pi/2
    alp4=np.pi/2; alp5=np.pi/2; alp6=0

    H06 = DH(T1,a1,d1,alp1) @ DH(T2,a2,d2,alp2) @ DH(T3,a3,d3,alp3) @ \
          DH(T4,a4,d4,alp4) @ DH(T5,a5,d5,alp5) @ DH(T6,a6,d6,alp6)

    H06[np.abs(H06) < 1e-10] = 0
    return H06


def cinematica_inversa(H):

    L1=109.99; L2=104.99; L3=94.09
    L4=50.75; L5=28.74; L6=56.47
    d6 = L5 + L6
    Px, Py, Pz = H[0,3], H[1,3], H[2,3]
    R06 = H[0:3,0:3]
    Pmx = Px - d6 * R06[0,2]
    Pmy = Py - d6 * R06[1,2]
    Pmz = Pz - d6 * R06[2,2]

    q1 = np.arctan2(Pmy, Pmx)
    r = np.sqrt(Pmx**2 + Pmy**2)
    D = (r**2 + (Pmz-L1)**2 - L2**2 - (L3+L4)**2) / (2*L2*(L3+L4))
    D = np.clip(D, -1, 1)
    q3 = np.arctan2(-np.sqrt(1-D**2), D)
    q2 = np.arctan2(Pmz-L1, r) - np.arctan2((L3+L4)*np.sin(q3), L2+(L3+L4)*np.cos(q3))

    def R(q, alp):
        return np.array([
            [np.cos(q), -np.cos(alp)*np.sin(q),  np.sin(alp)*np.sin(q)],
            [np.sin(q),  np.cos(alp)*np.cos(q), -np.sin(alp)*np.cos(q)],
            [0,          np.sin(alp),            np.cos(alp)]
        ])

    R03 = R(q1,np.pi/2) @ R(q2,0) @ R(q3,-np.pi/2)
    R36 = R03.T @ R06
    q5 = np.arctan2(np.sqrt(R36[2,0]**2 + R36[2,1]**2), R36[2,2])
    q4 = np.arctan2(R36[1,2], -R36[0,2])
    q6 = np.arctan2(R36[2,1], -R36[2,0])
    q = np.degrees([q1,q2,q3,q4,q5,q6])

    for i in range(6):
        if q[i] < 0:
            q[i] += 180

    return np.clip(q,0,180)


class Brazo_manipulador(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Interfaz.ui", self)
        self.setWindowTitle('Interfaz de control para un manipulador de 6 DOF')
        try:
            self.ser = serial.Serial('COM3', 9600, timeout=1)
        except:
            self.ser = None
            print("Sin conexión serial")

        self.pushButton.clicked.connect(self.gdatos)
        self.pushButton_CI_3.clicked.connect(self.calcular_CI)
        self.pushButton_copiar.clicked.connect(self.copiar_CD_a_CI)
        self.pushButton_guardar_A.clicked.connect(self.guardar_A)
        self.pushButton_guardar_B.clicked.connect(self.guardar_B)
        self.pushButton_trayectoria.clicked.connect(self.mover_trayectoria)

    def gdatos(self):
        q = [
            self.spinBox.value(),
            self.spinBox_2.value(),
            self.spinBox_3.value(),
            self.spinBox_4.value(),
            self.spinBox_5.value(),
            self.spinBox_6.value()
        ]
        H06 = cinematica_directa(q)
        self.mostrar_matriz(self.tabla_H06, H06)
        self.enviar_arduino(q)

    def calcular_CI(self):
        H = self.leer_tabla(self.tabla_H)
        q = cinematica_inversa(H)
        self.mostrar_q(q)
        self.enviar_arduino(q)

    def copiar_CD_a_CI(self):
        self.copiar_tabla(self.tabla_H06, self.tabla_H)

    def guardar_A(self):
        self.copiar_tabla(self.tabla_H06, self.tabla_A)

    def guardar_B(self):
        self.copiar_tabla(self.tabla_H06, self.tabla_B)

    def copiar_tabla(self, origen, destino):
        for i in range(4):
            for j in range(4):
                item = origen.item(i,j)
                valor = item.text() if item else "0"
                destino.setItem(i,j,QTableWidgetItem(valor))

    def leer_tabla(self, tabla):
        H = np.zeros((4,4))
        for i in range(4):
            for j in range(4):
                item = tabla.item(i,j)
                if item:
                    H[i,j] = float(item.text())
        return H

    def mostrar_q(self, q):
        for i in range(6):
            self.tabla_q.setItem(i,0,QTableWidgetItem(f"{q[i]:.2f}"))

    def mover_trayectoria(self):
        if self.ser is None:
            print("No hay conexión serial")
            return

        HA = self.leer_tabla(self.tabla_A)
        HB = self.leer_tabla(self.tabla_B)

        if np.all(HA == 0) or np.all(HB == 0):
            print("ERROR: A o B vacíos")
            return

        qA = cinematica_inversa(HA)
        qB = cinematica_inversa(HB)

        pasos = 5

        for i in range(pasos):

            t = i / (pasos - 1)
            q = qA + (qB - qA) * t
            q = np.array(q)
            q_corr = q.copy()
            q_corr[2] = np.clip(q_corr[2], 0, 180)
            comando = "Q1:{:.0f},Q2:{:.0f},Q3:{:.0f},Q4:{:.0f},Q5:{:.0f},Q6:{:.0f}\n".format(
            q_corr[0], q_corr[1], q_corr[2], q_corr[3], q_corr[4], q_corr[5]
        )
            print(comando)
            self.ser.write(comando.encode())
            self.ser.flush()
            QtWidgets.QApplication.processEvents()
            QtCore.QThread.msleep(700)

    def enviar_arduino(self, q):
        if self.ser:
            q_corr = q.copy()
            q_corr[2] = 180 - q_corr[2]
            comando = f"Q1:{q_corr[0]},Q2:{q_corr[1]},Q3:{q_corr[2]},Q4:{q_corr[3]},Q5:{q_corr[4]},Q6:{q_corr[5]}\n"
            self.ser.write(comando.encode())

    def mostrar_matriz(self, tabla, H):
        for i in range(4):
            for j in range(4):
                tabla.setItem(i,j,QTableWidgetItem(f"{H[i,j]:.3f}"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana = Brazo_manipulador()
    ventana.show()
    sys.exit(app.exec())