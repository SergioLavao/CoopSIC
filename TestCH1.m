%Comparison between OMA and CooperativeSIC with U2 fixed at Cell edge (max SR for CS)

clear all;
clc;

alpha = 3;
P_ce = 10; %0dB

dmax = 1;%meters
step = dmax/100;

c = 0;

[OMA, optimal_alpha,R1_OMA_N, R2_OMA_N, R1_CS, R2_CS] = deal(NaN*ones(1,c)); 

for d1 = step: step: dmax
    
    c = c + 1;
    
    R1_CS(c) = B*C( (P_ce*(d1.^-alpha)*(dmax^alpha)) );
    R2_CS(c) = B*C( P_ce./( 1 + P_ce ) );
    
    alpha_W = 0 : 0.01 : 1;
    
    for i = 1 : length(alpha_W)
        
        R1_OMA_temp(i) = alpha_W(i).*B.*C( (P_ce.*d1.^-alpha.*dmax.^alpha)./(N.*alpha_W(i)) );
        R2_OMA_temp(i) = (1-alpha_W(i)).*B.*C( P_ce./(N.*(1 - alpha_W(i))) );

        OMA_temp = R1_OMA_temp + R2_OMA_temp;

    end

    [OMA(c), i_x] = max( OMA_temp );
    optimal_alpha(c) = alpha_W(i_x);

    alpha_W = 0.5;

    R1_OMA_N(c) = alpha_W*B*C( (P_ce*d1.^-alpha*dmax^alpha)./(N*alpha_W) );
    R2_OMA_N(c) = (1-alpha_W)*B*C( P_ce./(N*(1 - alpha_W)) );


end

CS = R1_CS + R2_CS;
OMA_N = R1_OMA_N + R2_OMA_N;

d1 = step: step: dmax;

plot( d1,CS )
hold on
plot( d1,OMA )
hold on

figure 

plot( d1, ((CS ./ OMA) - 1) * 100 )
hold on
