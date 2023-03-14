function [CapOMA, alphas] = OptimalOMAN( P, W,N_0,alpha,d1x,d1y,d2x,d2y,d3x,d3y)

%Optimize alphas

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
CapOMA = alphas(1)*W*C(SNR1/alphas(1)) + alphas(2)*C(SNR2/alphas(2)) + alphas(3)*C(SNR3/alphas(3));

end