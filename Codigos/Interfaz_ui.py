# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Interfaz.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpinBox, QStatusBar,
    QTabWidget, QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(466, 568)
        MainWindow.setStyleSheet(u"QWidget {\n"
"    background-color: white;\n"
"    color: black;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 50, 441, 481))
        self.tabWidget.setStyleSheet(u"QWidget {\n"
"    background-color: #f5f6ff;\n"
"    color: #000000;\n"
"    font-family: Segoe UI;\n"
"    font-size: 12px;\n"
"}")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.spinBox = QSpinBox(self.tab)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(10, 40, 81, 23))
        self.spinBox.setMaximumSize(QSize(16777215, 23))
        self.spinBox.setStyleSheet(u"QSpinBox {\n"
"    background-color: white;\n"
"    color: black;\n"
"    border: 1px solid rgb(200, 200, 230);\n"
"    border-radius: 5px;\n"
"}")
        self.spinBox.setMaximum(180)
        self.spinBox_2 = QSpinBox(self.tab)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setGeometry(QRect(120, 40, 81, 23))
        self.spinBox_2.setMaximumSize(QSize(16777215, 23))
        self.spinBox_2.setStyleSheet(u"QSpinBox {\n"
"    background-color: white;\n"
"    color: black;\n"
"    border: 1px solid rgb(200, 200, 230);\n"
"    border-radius: 5px;\n"
"}")
        self.spinBox_2.setMaximum(180)
        self.spinBox_3 = QSpinBox(self.tab)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setGeometry(QRect(230, 40, 81, 23))
        self.spinBox_3.setMaximumSize(QSize(16777215, 23))
        self.spinBox_3.setStyleSheet(u"QSpinBox {\n"
"    background-color: white;\n"
"    color: black;\n"
"    border: 1px solid rgb(200, 200, 230);\n"
"    border-radius: 5px;\n"
"}")
        self.spinBox_3.setMaximum(180)
        self.spinBox_4 = QSpinBox(self.tab)
        self.spinBox_4.setObjectName(u"spinBox_4")
        self.spinBox_4.setGeometry(QRect(10, 110, 81, 23))
        self.spinBox_4.setMaximumSize(QSize(16777215, 23))
        self.spinBox_4.setStyleSheet(u"QSpinBox {\n"
"    background-color: white;\n"
"    color: black;\n"
"    border: 1px solid rgb(200, 200, 230);\n"
"    border-radius: 5px;\n"
"}")
        self.spinBox_4.setMaximum(180)
        self.spinBox_5 = QSpinBox(self.tab)
        self.spinBox_5.setObjectName(u"spinBox_5")
        self.spinBox_5.setGeometry(QRect(120, 110, 81, 23))
        self.spinBox_5.setMaximumSize(QSize(16777215, 23))
        self.spinBox_5.setStyleSheet(u"QSpinBox {\n"
"    background-color: white;\n"
"    color: black;\n"
"    border: 1px solid rgb(200, 200, 230);\n"
"    border-radius: 5px;\n"
"}")
        self.spinBox_5.setMaximum(180)
        self.spinBox_6 = QSpinBox(self.tab)
        self.spinBox_6.setObjectName(u"spinBox_6")
        self.spinBox_6.setGeometry(QRect(230, 110, 81, 23))
        self.spinBox_6.setMaximumSize(QSize(16777215, 23))
        self.spinBox_6.setStyleSheet(u"QSpinBox {\n"
"    background-color: white;\n"
"    color: black;\n"
"    border: 1px solid rgb(200, 200, 230);\n"
"    border-radius: 5px;\n"
"}")
        self.spinBox_6.setMaximum(180)
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 101, 31))
        self.tabla_H06 = QTableWidget(self.tab)
        if (self.tabla_H06.columnCount() < 4):
            self.tabla_H06.setColumnCount(4)
        if (self.tabla_H06.rowCount() < 4):
            self.tabla_H06.setRowCount(4)
        self.tabla_H06.setObjectName(u"tabla_H06")
        self.tabla_H06.setGeometry(QRect(10, 190, 421, 151))
        self.tabla_H06.setStyleSheet(u"QTableWidget {\n"
"    background-color: rgb(245, 244, 255);\n"
"    color: black;\n"
"    gridline-color: rgb(200, 200, 230);\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: rgb(215, 212, 255);\n"
"    color: black;\n"
"    font-weight: bold;\n"
"}")
        self.tabla_H06.setRowCount(4)
        self.tabla_H06.setColumnCount(4)
        self.pushButton = QPushButton(self.tab)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(350, 420, 79, 24))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(215, 212, 255);\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"    border: 1px solid rgb(180, 180, 230);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(200, 195, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(170, 165, 240);\n"
"}")
        self.pushButton_copiar = QPushButton(self.tab)
        self.pushButton_copiar.setObjectName(u"pushButton_copiar")
        self.pushButton_copiar.setGeometry(QRect(10, 360, 81, 24))
        self.pushButton_copiar.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(215, 212, 255);\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"    border: 1px solid rgb(180, 180, 230);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(200, 195, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(170, 165, 240);\n"
"}")
        self.pushButton_guardar_A = QPushButton(self.tab)
        self.pushButton_guardar_A.setObjectName(u"pushButton_guardar_A")
        self.pushButton_guardar_A.setGeometry(QRect(100, 360, 111, 24))
        self.pushButton_guardar_A.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(215, 212, 255);\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"    border: 1px solid rgb(180, 180, 230);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(200, 195, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(170, 165, 240);\n"
"}")
        self.pushButton_guardar_B = QPushButton(self.tab)
        self.pushButton_guardar_B.setObjectName(u"pushButton_guardar_B")
        self.pushButton_guardar_B.setGeometry(QRect(220, 360, 111, 24))
        self.pushButton_guardar_B.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(215, 212, 255);\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"    border: 1px solid rgb(180, 180, 230);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(200, 195, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(170, 165, 240);\n"
"}")
        self.label_8 = QLabel(self.tab)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(120, 10, 101, 31))
        self.label_9 = QLabel(self.tab)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(230, 10, 101, 31))
        self.label_10 = QLabel(self.tab)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(120, 80, 101, 31))
        self.label_11 = QLabel(self.tab)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(10, 80, 101, 31))
        self.label_12 = QLabel(self.tab)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(230, 80, 101, 31))
        self.label_13 = QLabel(self.tab)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(20, 160, 141, 16))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabla_H = QTableWidget(self.tab_2)
        if (self.tabla_H.columnCount() < 4):
            self.tabla_H.setColumnCount(4)
        if (self.tabla_H.rowCount() < 4):
            self.tabla_H.setRowCount(4)
        self.tabla_H.setObjectName(u"tabla_H")
        self.tabla_H.setGeometry(QRect(10, 40, 421, 151))
        self.tabla_H.setStyleSheet(u"QTableWidget {\n"
"    background-color: rgb(245, 244, 255);\n"
"    color: black;\n"
"    gridline-color: rgb(200, 200, 230);\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: rgb(215, 212, 255);\n"
"    color: black;\n"
"    font-weight: bold;\n"
"}")
        self.tabla_H.setRowCount(4)
        self.tabla_H.setColumnCount(4)
        self.pushButton_CI = QPushButton(self.tab_2)
        self.pushButton_CI.setObjectName(u"pushButton_CI")
        self.pushButton_CI.setGeometry(QRect(680, 470, 79, 24))
        self.tabla_q = QTableWidget(self.tab_2)
        if (self.tabla_q.columnCount() < 1):
            self.tabla_q.setColumnCount(1)
        if (self.tabla_q.rowCount() < 6):
            self.tabla_q.setRowCount(6)
        self.tabla_q.setObjectName(u"tabla_q")
        self.tabla_q.setGeometry(QRect(10, 230, 121, 211))
        self.tabla_q.setStyleSheet(u"QTableWidget {\n"
"    background-color: rgb(245, 244, 255);\n"
"    color: black;\n"
"    gridline-color: rgb(200, 200, 230);\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: rgb(215, 212, 255);\n"
"    color: black;\n"
"    font-weight: bold;\n"
"}")
        self.tabla_q.setRowCount(6)
        self.tabla_q.setColumnCount(1)
        self.label_4 = QLabel(self.tab_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 10, 251, 16))
        self.label_5 = QLabel(self.tab_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 200, 191, 21))
        self.pushButton_CI_3 = QPushButton(self.tab_2)
        self.pushButton_CI_3.setObjectName(u"pushButton_CI_3")
        self.pushButton_CI_3.setGeometry(QRect(350, 420, 79, 24))
        self.pushButton_CI_3.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(215, 212, 255);\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"    border: 1px solid rgb(180, 180, 230);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(200, 195, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(170, 165, 240);\n"
"}")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.pushButton_trayectoria = QPushButton(self.tab_3)
        self.pushButton_trayectoria.setObjectName(u"pushButton_trayectoria")
        self.pushButton_trayectoria.setGeometry(QRect(308, 420, 121, 24))
        self.pushButton_trayectoria.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(215, 212, 255);\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"    border: 1px solid rgb(180, 180, 230);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(200, 195, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(170, 165, 240);\n"
"}")
        self.tabla_A = QTableWidget(self.tab_3)
        if (self.tabla_A.columnCount() < 4):
            self.tabla_A.setColumnCount(4)
        if (self.tabla_A.rowCount() < 4):
            self.tabla_A.setRowCount(4)
        self.tabla_A.setObjectName(u"tabla_A")
        self.tabla_A.setGeometry(QRect(0, 50, 421, 151))
        self.tabla_A.setStyleSheet(u"QTableWidget {\n"
"    background-color: rgb(245, 244, 255);\n"
"    color: black;\n"
"    gridline-color: rgb(200, 200, 230);\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: rgb(215, 212, 255);\n"
"    color: black;\n"
"    font-weight: bold;\n"
"}")
        self.tabla_A.setRowCount(4)
        self.tabla_A.setColumnCount(4)
        self.tabla_B = QTableWidget(self.tab_3)
        if (self.tabla_B.columnCount() < 4):
            self.tabla_B.setColumnCount(4)
        if (self.tabla_B.rowCount() < 4):
            self.tabla_B.setRowCount(4)
        self.tabla_B.setObjectName(u"tabla_B")
        self.tabla_B.setGeometry(QRect(0, 250, 421, 151))
        self.tabla_B.setStyleSheet(u"QTableWidget {\n"
"    background-color: rgb(245, 244, 255);\n"
"    color: black;\n"
"    gridline-color: rgb(200, 200, 230);\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: rgb(215, 212, 255);\n"
"    color: black;\n"
"    font-weight: bold;\n"
"}")
        self.tabla_B.setRowCount(4)
        self.tabla_B.setColumnCount(4)
        self.label_6 = QLabel(self.tab_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 20, 141, 21))
        self.label_7 = QLabel(self.tab_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 220, 141, 21))
        self.tabWidget.addTab(self.tab_3, "")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(90, 10, 271, 41))
        self.label_2.setMinimumSize(QSize(141, 41))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Articulaci\u00f3n 1:</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Ejecutar", None))
        self.pushButton_copiar.setText(QCoreApplication.translate("MainWindow", u"Mandar a CI", None))
        self.pushButton_guardar_A.setText(QCoreApplication.translate("MainWindow", u"Guardar posici\u00f3n A", None))
        self.pushButton_guardar_B.setText(QCoreApplication.translate("MainWindow", u"Guardar posici\u00f3n B", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Articulaci\u00f3n 2:</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Articulaci\u00f3n 3:</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Articulaci\u00f3n 5:</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Articulaci\u00f3n 4:</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Articulaci\u00f3n 6:</span></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Matriz homog\u00e9nea:</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Cinem\u00e1tica directa ", None))
        self.pushButton_CI.setText(QCoreApplication.translate("MainWindow", u"Ejecutar", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Colocar la posici\u00f3n y orientaci\u00f3n deseadas:</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Resultados de cada articulaci\u00f3n:</span></p></body></html>", None))
        self.pushButton_CI_3.setText(QCoreApplication.translate("MainWindow", u"Ejecutar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Cinem\u00e1tica inversa ", None))
        self.pushButton_trayectoria.setText(QCoreApplication.translate("MainWindow", u"Ejecutar Trayectoria", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Colocarla posici\u00f3n A:</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Colocarla posici\u00f3n B:</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Trayectoria", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">Brazo manipulador de 6GDL</span></p></body></html>", None))
    # retranslateUi

