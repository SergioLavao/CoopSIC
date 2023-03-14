P_ce = 10; %dB at cell edge
P = 10.^(P_ce/10);

CRPairUsers( P, 3, [0,-0.5], [0,1], "SIC Gain 1" )