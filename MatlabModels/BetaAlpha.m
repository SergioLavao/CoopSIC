c = 0;
R1_ = 0.01 : 0.01 : 1;
[R2_x, a_x, b_x] = deal(NaN*ones(1,c));

for R1 = 0.01 : 0.01 : 1

    c = c + 1;
    alpha = 0.01 : 0.01 : 1;
        
    beta = alpha.*(2.^(R1./alpha) - 1);
    beta(beta>1) = NaN;
    R2 = NaN*ones(100,1);

    for i = 1 : length(alpha)

        R2(i) = (1 - alpha(i))*log2( 1 + (1 - beta(i)).*100./(1 - alpha(i)) ); 

    end

    [R2_x(c),i_x] = max(R2);
    b_x(c) = beta(i_x);
    a_x(c) = alpha(i_x);

end

figure
plot(R1_,R2_x)