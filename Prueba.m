%Comparison between OMA and CooperativeSIC with U2 fixed at Cell edge (max SR for CS)

clear all;
clc;

maxdB = 40;

for SNRce_vec = -20:5:maxdB

c = 0;

for SNR1_vec = maxdB: -1: SNRce_vec %from 20dB to 0dB
    
    SNRce = 10^(SNRce_vec/10);
    SNR1 = 10^(SNR1_vec/10);

    c = c + 1;
    
    SR_CS(c) = C(SNR1) + C( SNRce / (1 + SNRce) );
    
    alpha_W = 0 : 0.001 : 1;
    

    for i = 1 : length(alpha_W)
        
        R1_OMA_temp(i) = alpha_W(i).*C( SNR1 ./alpha_W(i) );
        R2_OMA_temp(i) = ( 1 - alpha_W(i) ).*C( SNRce ./( 1 - alpha_W(i) ) );

        SR_OMA_temp(i) = R1_OMA_temp(i) + R2_OMA_temp(i);

    end

    [SR_OMA(c), i_x] = max( SR_OMA_temp );
    optimal_alpha(c) = alpha_W(i_x);

end

SNR1_vec = maxdB: -1: SNRce_vec;

% plot( SR_OMA )
% hold on
plot( SNR1_vec, SR_CS./SR_OMA )
hold on
grid on
% 

clear SR_CS SR_OMA;

end

ylabel("SR")
xlabel("SNR1")
