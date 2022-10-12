clear
%Comparison between OMA(OFDM) vs NOMA(PDM)
%OFDM Must use power split P = P1 + P2. Same as PDM

filename = 'OMAvsNOMA.gif';
c = 0;

%Alpha optimization to compute the boundary on OMA
for beta = 0 : 0.01 : 1
    clf
    c = c+1;
    alpha = 0:0.01:1;
    
    P = 1;
    P_1 = beta*P*1;
    P_2 = (1 - beta)*P*100;
    
    %Alpha optimization to compute the boundary on OMA
    R1_OMA = alpha.*log2(1 + P_1./alpha);
    R2_OMA = (1 - alpha).*log2(1 + P_2./(1 - alpha));
    
    [SR_max(c), idx] = max(R1_OMA+R2_OMA);
    alpha_max(c) = alpha(idx);
    R1_max(c) = R1_OMA(idx);
    R2_max(c) = R2_OMA(idx);
    %alpha
    
    R1_NOMA = log2(1 + P_1);
    R2_NOMA = log2(1 + P_2./(1 + P_1));
    
    plot(R1_OMA,R2_OMA)
    hold on
    plot(R1_max,R2_max,'r*')
    plot(R1_NOMA,R2_NOMA)
    hold on
    grid on
    
    legend('OMA','NOMA')
    xlabel('Capacity User 1')
    ylabel('Capacity User 2')
    
    drawnow
          
end