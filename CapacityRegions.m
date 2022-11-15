P_ce = 0; %dB at cell edge
P = 10.^(P_ce/10);

subplot(2,2,1);
CRPairUsers( P, [-0.9,-0.1], [0.3,0.85], "SIC Gain 1" )
subplot(2,2,2);
CRPairUsers( P, [-0.4,-0.3], [0.3,0.85], "SIC Gain 2" )
subplot(2,2,3);
CRPairUsers( P, [0,-1], [0.3,0.85], "SIC Gain 3" )
subplot(2,2,4);
CRPairUsers( P, [0.8,-0.2], [0.3,0.85], "SIC Gain 4" )