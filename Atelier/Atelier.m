
%% Problème 2.1
clc
clear
close all

% Fonction pour le temps
dt = 0.01;
t = 0:dt:10;

% Fonction cosinus (Elle prends en radiant)
Y = cos(2*pi*t);

%Fonction cosinus en degré
%Y = cosd(2*t)

%Façon 1 de ploter (Ca fait une ligne)
subplot(2, 1, 1)
plot(t, Y);
title('Cosinus en Rad');
xlabel('Temps');
ylabel('Amplitude');

%Façon 2 de ploter (Ça mets des points partout)
subplot(2, 1, 2)
scatter(t, Y, '+', 'red');
title('Points en scatter');
xlabel('Temps');
ylabel('Amplitude');

%% Problème 2.2
%Juste prendre de 2 à 4
t2 = t(2/dt + 1: 4/dt + 1);
Y2 = cos(2*pi*t2);

%Juste prendre de 9 à 10
t3 = t(9/dt + 1: 10/dt + 1);
Y3 = cos(2*pi*t3);

% .^2 mets au carrer
figure;
plot(t2, Y2.^2);
hold on
plot(t3, abs(Y3));

title('f(A)^2 de 2s à 4s et de 9s à 10s')
xlabel('Temps');
ylabel('Amplitude');

