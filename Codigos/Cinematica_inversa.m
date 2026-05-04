clear all; clc; close all;

L1 = 109.99; L2 = 104.99; L3 = 94.09; L4 = 50.75; L5 = 28.74; L6 = 56.47;

d1 = L1;
a2 = L2;
d4 = L3 + L4;
d6 = L5 + L6;

H_objetivo = [ 0.5766   0.0996  -0.8110  -211.1367;
    0.8149  -0.1422   0.5619   250.7242;
    -0.0594  -0.9848  -0.1632    70.9346;
    0        0        0          1.0000];

Px = H_objetivo(1,4);
Py = H_objetivo(2,4);
Pz = H_objetivo(3,4);

R06 = H_objetivo(1:3, 1:3);

Pmx = Px - d6 * R06(1,3);
Pmy = Py - d6 * R06(2,3);
Pmz = Pz - d6 * R06(3,3);

q1 = atan2(Pmy, Pmx);
r  = sqrt(Pmx^2 + Pmy^2);

D = (r^2 + (Pmz-L1)^2 - L2^2 - (L3+L4)^2) / (2*L2*(L3+L4));

q3 = atan2(-sqrt(1-D^2), D);
q2 = atan2(Pmz-L1, r) - atan2((L3+L4)*sin(q3), L2+(L3+L4)*cos(q3));

alp1 =  pi/2;
alp2 =  0;
alp3 = -pi/2;

R01 = [ cos(q1) -cos(alp1)*sin(q1)  sin(alp1)*sin(q1);
    sin(q1)  cos(alp1)*cos(q1) -sin(alp1)*cos(q1);
    0        sin(alp1)          cos(alp1)];

R12 = [ cos(q2) -cos(alp2)*sin(q2)  sin(alp2)*sin(q2);
    sin(q2)  cos(alp2)*cos(q2) -sin(alp2)*cos(q2);
    0        sin(alp2)          cos(alp2)];

R23 = [ cos(q3) -cos(alp3)*sin(q3)  sin(alp3)*sin(q3);
    sin(q3)  cos(alp3)*cos(q3) -sin(alp3)*cos(q3);
    0        sin(alp3)          cos(alp3)];

R03 = R01 * R12 * R23;
R36 = R03' * R06;

q5 = atan2(sqrt(R36(3,1)^2 + R36(3,2)^2), R36(3,3));
q4 = atan2(R36(2,3), -R36(1,3));
q6 = atan2(R36(3,2), -R36(3,1));

q3_display = q3;
if rad2deg(q3_display) < 0
    q3_display = q3_display + pi;
end

deg_q4 = rad2deg(q4);
deg_q5 = rad2deg(q5);

fprintf('--- Solución 1 ---\n');
fprintf('q1 = %.2f°\n', rad2deg(q1));
fprintf('q2 = %.2f°\n', rad2deg(q2));
fprintf('q3 = %.2f°\n', rad2deg(q3_display));
fprintf('q4 = %.2f°\n', deg_q4);
fprintf('q5 = %.2f°\n', deg_q5);
fprintf('q6 = %.2f°\n', rad2deg(q6));

tol = 1e-2;

if abs(deg_q4) < tol
    fprintf('Posible solucion: q4_2 = 180°\n');
elseif abs(abs(deg_q4) - 180) < tol
    fprintf('Posible solucion: q4_2 = 0°\n');
end

if abs(deg_q5) < tol
    fprintf('Posible solucion: q5_2 = 180°\n');
elseif abs(abs(deg_q5) - 180) < tol
    fprintf('Posible solucion: q5_2 = 0°\n');
end

disp('R36');
disp(R36);