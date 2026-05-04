clear all; clc; close all;

q1 = deg2rad(125);
q2 = deg2rad(0);
q3 = deg2rad(170);
q4 = deg2rad(90);
q5 = deg2rad(70);
q6 = deg2rad(0)

L1 = 109.99; L2 = 104.99; L3 = 94.09; L4 = 50.75; L5 = 28.74; L6 = 56.47;

T1 = q1; 
T2 = q2; 
T3 = q3 + pi/2;
T4 = q4; 
T5 = q5 + pi/2;
T6 = q6;

d1 = L1;      d2 = 0;       d3 = 0;
d4 = L3 + L4; d5 = 0;       d6 = L5 + L6;

a1 = 0;       a2 = L2;      a3 = 0;
a4 = 0;       a5 = 0;       a6 = 0;

alp1 = pi/2;  alp2 = 0;     alp3 = -pi/2;
alp4 = pi/2;  alp5 = pi/2;  alp6 = 0;

H_base = eye(4);
H_base(3,4) = 0;

DH = @(T,a,d,alp)[ ...
    cos(T) -cos(alp)*sin(T)  sin(alp)*sin(T) a*cos(T);
    sin(T)  cos(alp)*cos(T) -sin(alp)*cos(T) a*sin(T);
    0       sin(alp)         cos(alp)        d;
    0       0                0               1];

H1 = DH(T1, a1, d1, alp1);
H2 = DH(T2, a2, d2, alp2);
H3 = DH(T3, a3, d3, alp3);
H4 = DH(T4, a4, d4, alp4);
H5 = DH(T5, a5, d5, alp5);
H6 = DH(T6, a6, d6, alp6);

H0  = H_base;
H01 = H0  * H1;
H02 = H01 * H2;
H03 = H02 * H3;
H04 = H03 * H4;
H05 = H04 * H5;
H06 = H05 * H6;

h = H3 * H4 * H5 * H6

P = [H0(1:3,4),  H01(1:3,4), H02(1:3,4), ...
     H03(1:3,4), H04(1:3,4), H05(1:3,4), H06(1:3,4)];

figure
plot3(P(1,:), P(2,:), P(3,:), '-o', ...
      'LineWidth', 2, 'MarkerSize', 7, 'MarkerFaceColor', 'b')
hold on
plot3(P(1,6), P(2,6), P(3,6), 'ro', 'MarkerSize', 10, 'LineWidth', 2)
text(P(1,6), P(2,6), P(3,6), '  Centro muñeca', 'Color', 'r', 'FontSize', 10)
grid on
axis equal
xlabel('X')
ylabel('Y')
zlabel('Z')
title('Configuración 4 CD')
view(45,30)

H06(abs(H06) < 1e-10) = 0;
disp('H06')
disp(H06)