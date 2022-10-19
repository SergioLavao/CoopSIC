c = 0; %Define a counter for vector indexes

R1_ = 0.01 : 0.01 : 1; %Define R1 vector from 0 to max User 1 Capity
[R2_x, a_x, b_x] = deal(NaN*ones(1,c)); %Pre allocating vector sizes 

for R1 = 0.01 : 0.01 : 1 %For each R1 value, assign a optimized alpha and beta

    c = c + 1; %Vector index + 1

    alpha = 0.01 : 0.01 : 1; %Set a vector of alpha ( For each alpha optimize beta )

    beta = alpha.*(2.^(R1./alpha) - 1); %From C(x) clear beta variable
    beta(beta>1) = NaN; %Due to the limits, 0 <|= beta <|= 1, if not NaN value
    R2 = NaN*ones(100,1); %R2 size = R1 size

    for i = 1 : length(alpha) %For each alpha, get a R2 Capacity vector

       R2(i) = (1 - alpha(i))*log2( 1 + (1 - beta(i)).*100./(1 - alpha(i)) ); % C(x)

    end

    [R2_x(c),i_x] = max(R2); %With R2 for each alpha, find max R2 value, vector index
    b_x(c) = beta(i_x); %Get beta optimal value
    a_x(c) = alpha(i_x); %Get alpha optimal value

    %R2_x represents the vector with maximum values for each R1
    %And we get it, yeyy :)

end

plot(R1_,R2_x) %Plot Capacity regions