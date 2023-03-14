P = 100;
h1 = 1/20;
h2 = 1/100;

beta = 0:0.01:1;

R1 = beta.*log2(P*h1./beta);
R2 = (1-beta).*log2(P*h2./(1-beta));
cap = R1 + R2;

plot( beta,cap )
