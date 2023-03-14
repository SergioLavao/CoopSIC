%Variable Channel gains comparison OMA vs NOMA

RateVectorSize = 100;

maxh2Gain = 10;

P = 1;
h2_ = maxh2Gain;

c = 0;

for h1_ = 0 : 1 : maxh2Gain

    clf
    
    c = c + 1;

    h1 = 10^(h1_/10);
    h2 = 10^(h2_/10);

    [R1_OMA , R2_OMA] = OptimalOMA( P, h1, h2, RateVectorSize, true );
    
    beta = 0:0.01:1;
    
    P_1 = beta*P*h1;
    P_2 = (1 - beta)*P*h2;
    
    R1_NOMA = log2(1 + P_1);
    R2_NOMA = log2(1 + P_2./(1 + P_1));
    plot(R1_NOMA,R2_NOMA)
    xlabel("R1 [bps/Hz]")
    ylabel("R2 [bps/Hz]")
    
    xlim( [ 0 , log2( 1 + P*h1 ) ] )
    
    hold on

    strTitle = "P|h1| = " + num2str( 10*log10(P*h1) ) + "[dB]" + ", P|h2| = " + num2str( 10*log10(P*h2) ) + "[dB]";

    title( strTitle )

    pause(.5)

end
