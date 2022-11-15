%Returns the capacity region for 2 users without power split
function [R1_OMA_FS, R2_OMA_FS] = OptimalOMAFullPS( P,h1,h2,RateVectorSize, b_plotOMA )

    c = 0;
    max_R1 = log2( 1 + P*h1 );
    
    Rstep = max_R1/RateVectorSize;
    R1_ = Rstep : Rstep : max_R1;
    
    R2_x = deal(NaN*ones(1,c)); 

    R2_x(0) = log2( 1 + P*h2 );
    R1_(end) = max_R1;

    for R1 = Rstep : Rstep : max_R1 
        
        c = c + 1;
        
        R2_x(c) = 0;

        for alpha = 0 : 0.01 : 1
            
            R1_x = alpha*log2(1 + P*h1/alpha);
            
            if R1 == R1_x

                R2_x(c) = (1 - alpha)*log2( 1 + P*h2/(1 - alpha) );
                   
            end 

        end

    end
    
    if b_plotOMA
        %clf
        plot(R1_,R2_x)
        hold on
    end

    R1_OMA_FS = R1_;
    R2_OMA_FS = R2_x;

end