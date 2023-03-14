function [CapOMAOCI, alphas] = OCIOptimalOMAN( P,W,N_0,alpha,d1x,d1y,d2x,d2y,d3x,d3y)

%Optimize alphas

OCI_User1 = P./(3.0.*(0.333.*(-0.577.*d1x - 1.0).^2 + (-0.333.*d1y - 1.0).^2).^0.5).^alpha + P./(1.73.*(0.333.*(1.0 - d1y).^2 + (-0.577.*d1x - 1.0).^2).^0.5).^alpha + P./(1.73.*((1.0 - 0.577.*d1x).^2 + 0.333.*(-d1y - 1.0).^2).^0.5).^alpha;
OCI_User2 = P./(3.0.*((1.0 - 0.333.*d2y).^2 + 0.333.*(-0.577.*d2x - 1.0).^2).^0.5).^alpha + P./(1.73.*((-0.577.*d2x - 1.0).^2 + 0.333.*(-d2y - 1.0).^2).^0.5).^alpha + P./(1.73.*((1.0 - 0.577.*d2x).^2 + 0.333.*(1.0 - d2y).^2).^0.5).^alpha;
OCI_User3 = P./(3.46.*(0.0833.*d3y.^2 + (1.0 - 0.289.*d3x).^2).^0.5).^alpha + P./(2.0.*(0.25.*d3x.^2 + (-0.5.*d3y - 1.0).^2).^0.5).^alpha + P./(2.0.*(0.25.*d3x.^2 + (1.0 - 0.5.*d3y).^2).^0.5).^alpha;

alpha0 = [0,0,0];
A = [1,1,1];
b = 1;

lb = [0,0,0];
ub = [1,1,1];

Aeq = [0,0,0 ];
beq = 0;

SNR1 = P*sqrt(d1x^2+ d1y^2)^-(alpha)./(N_0*W);
SNR2 = P*sqrt(d2x^2+ d2y^2)^-(alpha)./(N_0*W);
SNR3 = P*sqrt(d3x^2+ d3y^2)^-(alpha)./(N_0*W);

fun = @(alphas) -( alphas(1)*W*C(SNR1/alphas(1)) + alphas(2)*C(SNR2/alphas(2)) + alphas(3)*C(SNR3/alphas(3)) );

alphas = fmincon(fun,alpha0,A,b,Aeq,beq,lb,ub);
CapOMAOCI = alphas(1)*W*C(SNR1/(alphas(1) + OCI_User1)) + alphas(2)*C(SNR2/(alphas(2) + OCI_User2)) + alphas(3)*C(SNR3/(alphas(3) + OCI_User3));

end