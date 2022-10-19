function [R1_OMA, R2_OMA] = OptimalOMA(P,h1,h2,RateVectorSize, b_plotOMA)

    c = 0; 
    max_R1 = log2( 1 + P*h1 );
    
    Rstep = max_R1/RateVectorSize;
    R1_ = Rstep : Rstep : max_R1;
    
    [R2_x, a_x, b_x] = deal(NaN*ones(1,c)); 
        
    for R1 = Rstep : Rstep : max_R1 
        
        c = c + 1;
        
        alpha = 0.01 : 0.01 : 1;
        beta = alpha.*(2.^(R1./alpha) - 1)./(P*h1); 
        beta(beta>1) = NaN; 
        R2 = NaN*ones(RateVectorSize,1); 
        
        for i = 1 : length(alpha)
           R2(i) = (1 - alpha(i))*log2( 1 + (1 - beta(i)).*P.*h2./(1 - alpha(i)) );
        end
        
        [R2_x(c),i_x] = max(R2);
        b_x(c) = beta(i_x);
        a_x(c) = alpha(i_x);
        
    end
    
    if b_plotOMA
        %clf
        plot(R1_,R2_x)
        hold on
    end

    R1_OMA = R1_;
    R2_OMA = R2_x;

end