%Comparison between OMA and CooperativeSIC with U2 fixed at Cell edge (max SR for CS)

clear all;
clc;

alpha = 3;
P_ce = 1; %0dB

dmax = 1;
step = dmax/100;
d1 = step:step:dmax;%[meters]

B = 1; %bandwidth 5MHz
N0 = 10^-21; %-150 dBw/Hz 
N = 1; % dBW

alpha_W = 0.5;

R1_OMA = alpha_W*B*C( (P_ce*d1.^-alpha*dmax^alpha)./(N*alpha_W) );
R2_OMA = (1-alpha_W)*B*C( P_ce./(N*(1 - alpha_W)) );

R1_CS = B*C( (P_ce*d1.^-alpha*dmax^alpha)./N );
R2_CS = B*C( P_ce./( N + P_ce ) );

CS = R1_CS + R2_CS;
OMA = R1_OMA + R2_OMA;

plot( CS )
hold on
plot( OMA )