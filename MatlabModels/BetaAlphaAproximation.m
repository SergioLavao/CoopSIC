c = 1;

for beta = 0.01 : 0.01 : 1
       
    c = c + 1;

    alpha = 1 - beta;
    
    P = 1;
    sigma = 0.5;
    P1 = beta*P;
    P2 = (1 - beta)*P;

    Ph1 = P1/beta;
    Ph2 = P2*100/(1 - beta);

    R1_OMA(c) = beta*log2( 1 + Ph1/beta );
    R2_OMA(c) = (1 - beta)*log2( 1 + Ph2/(1 - beta) );

    beta_vec(c) = beta;

end

hold on
plot( R1_OMA, R2_OMA )
