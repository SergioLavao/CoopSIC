%Comparison between OMA and CooperativeSIC with U2 fixed at Cell edge (max SR for CS)

clear all;
clc;

SNR1 = 1;%20 dB
SNR2 = 1;%0 dB at cell edge

c = 0;
    
SR_CS = C(SNR1) + C( SNR2 / (1 + SNR2) )
    
alpha = 0.001 : 0.001 : 1;
for i = 1 : length(alpha)
    SR_OMA_temp(i) = alpha(i)*C( SNR1 /alpha(i) ) + ( 1 - alpha(i) )*C( SNR2 /( 1 - alpha(i) ) );
end

[SR_OMA, i_x] = max( SR_OMA_temp );
SR_OMA
optimal_alpha = alpha(i_x)