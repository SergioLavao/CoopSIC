P = 1;
W = 1;
N_0 = 1;
rho = 1;
alpha = 1;

d1x = 1:0.01:3.5;
d1y = 2:0.01:4.5;
BS1Pos = [2.30940108 3.28867513];
U2Pos = [2.30940108 2.28867513];
BS2Pos = [2.30940108 1.28867513];

[d1x , d1y] = meshgrid(d1x,d1y);

BS1polygonX = [3.46410162 2.88675135 1.73205081 1.15470054 1.73205081 2.88675135 3.46410162];
BS1polygonY = [3.28867513 4.28867513 4.28867513 3.28867513 2.28867513 2.28867513 3.28867513];

[in,on] = inpolygon(d1x,d1y,BS1polygonX,BS1polygonY);

d1x_rel = d1x - BS1Pos(1);
d1y_rel = d1y - BS1Pos(2);

C_CoopSIC_User1 = (W.*rho).*log2(1 + P./((2.0.*(0.25.*d1x_rel.^2 + (-0.5.*d1y_rel - 1.0).^2).^0.5).^alpha.*(N_0.*W.*rho + P./(d1x_rel.^2 + d1y_rel.^2).^(0.5.*alpha))));
C_CoopSIC_User2 = (W.*rho).*log2(1 + P./(N_0.*W.*rho.*(d1x_rel.^2 + d1y_rel.^2).^(0.5.*alpha)));
CoopSIC = C_CoopSIC_User1+C_CoopSIC_User2;
C_OMA_User1 = (0.5.*W.*rho).*log2(1 + 2.0.*P./(1.0.^alpha.*N_0.*W.*rho));
C_OMA_User2 = (0.5.*W.*rho).*log2(1 + 2.0.*P./(N_0.*W.*rho.*(d1x_rel.^2 + d1y_rel.^2).^(0.5.*alpha)));
OMA = C_OMA_User1+C_OMA_User2;
C_IaN_User1 = (W.*rho).*log2(1 + P./(1.0.^alpha.*(N_0.*W.*rho + P./1.0.^alpha)));
C_IaN_User2 = (W.*rho).*log2(1 + P./((d1x_rel.^2 + d1y_rel.^2).^(0.5.*alpha).*(N_0.*W.*rho + P./(2.0.*(0.25.*d1x_rel.^2 + (-0.5.*d1y_rel - 1.0).^2).^0.5).^alpha)));
IaN = C_IaN_User1+C_IaN_User2;

BS1polygonX = [3.46410162 2.88675135 1.73205081 1.15470054 1.73205081 2.88675135 3.46410162];
BS1polygonY = [3.28867513 4.28867513 4.28867513 3.28867513 2.28867513 2.28867513 3.28867513];
BS2polygonX = [3.46410162 2.88675135 1.73205081 1.15470054 1.73205081 2.88675135 3.46410162];
BS2polygonY = [1.28867513 2.28867513 2.28867513 1.28867513 0.28867513 0.28867513 1.28867513];

figure

plot(BS1polygonX,BS1polygonY)
hold on
plot(BS2polygonX,BS2polygonY)
plot( U2Pos(1),U2Pos(2),'o','MarkerFaceColor','r');

%IMPORTANTE
CoopSIC = CoopSIC .* in;
CoopSIC(CoopSIC==0) = NaN;
CoopSIC(CoopSIC>5) = 5;
surf(d1x,d1y,CoopSIC, 'EdgeColor','none', 'FaceColor', '#77AC30', 'FaceAlpha', 1)

%IMPORTANTE
OMA = OMA .* in;
OMA(OMA==0) = NaN;
OMA(OMA>5) = 5;
surf(d1x,d1y,OMA, 'EdgeColor','none', 'FaceColor', '#0072BD', 'FaceAlpha', 1)

%IMPORTANTE
IaN = IaN .* in;
IaN(IaN==0) = NaN;
IaN(IaN>5) = 5;
surf(d1x,d1y,IaN, 'EdgeColor','none', 'FaceColor', '#D95319', 'FaceAlpha', 1)

grid on
ylim( [0 4.5] )
xlim( [0 4.5] )