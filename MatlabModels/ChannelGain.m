

P_11 = P./(d1x.^2 + d1y.^2).^(0.5.*alpha);
P_12 = P./(2.0.*(0.25.*d1x.^2 + (-0.5.*d1y - 1.0).^2).^0.5).^alpha;
P_13 = P./(1.73.*((-0.577.*d1x - 1.0).^2 + 0.333.*(-d1y - 1.0).^2).^0.5).^alpha;
P_21 = P./(2.0.*(0.25.*d2x.^2 + (1.0 - 0.5.*d2y).^2).^0.5).^alpha;
P_22 = P./(d2x.^2 + d2y.^2).^(0.5.*alpha);
P_23 = P./(1.73.*(0.333.*(1.0 - d2y).^2 + (-0.577.*d2x - 1.0).^2).^0.5).^alpha;
P_31 = P./(1.73.*((1.0 - 0.577.*d3x).^2 + 0.333.*(1.0 - d3y).^2).^0.5).^alpha;
P_32 = P./(1.73.*((1.0 - 0.577.*d3x).^2 + 0.333.*(-d3y - 1.0).^2).^0.5).^alpha;
P_33 = P./(d3x.^2 + d3y.^2).^(0.5.*alpha);