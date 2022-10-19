clear
%Variable Channel gains comparison OMA vs NOMA

enableRealTimePlot = false;

RateVectorSize = 100;

maxh2Gain = 60;

P = 1;
h2_ = maxh2Gain;

c = 0;

[relativeGain, h1_plot] = deal(NaN*ones(1,c)); 

for h1_ = -40 : 1 : maxh2Gain
    
    c = c + 1;

    h1 = 10^(h1_/10);
    h2 = 10^(h2_/10);

    [R1_OMA , R2_OMA] = OptimalOMA( P, h1, h2, RateVectorSize, enableRealTimePlot );
    
    beta = 0:0.01:1;
    
    P_1 = beta*P*h1;
    P_2 = (1 - beta)*P*h2;
    
    R1_NOMA = log2(1 + P_1);
    R2_NOMA = log2(1 + P_2./(1 + P_1));
    AreaOMA = sum( R1_OMA ) + sum( R2_OMA(~isnan(R2_OMA)) );
    AreaNOMA = sum( R1_NOMA ) + sum( R2_NOMA );

    tempRelativeGain = AreaNOMA / AreaOMA;
    tempRelativeGain = (tempRelativeGain - 1) * 100;

    relativeGain(c) = tempRelativeGain;
    h1_plot(c) = h1_;

    if enableRealTimePlot

        plot(R1_NOMA,R2_NOMA)
        xlabel("R1 [bps/Hz]")
        ylabel("R2 [bps/Hz]")
        
        xlim( [ 0 , log2( 1 + P*h1 ) ] )
    
        strTitle = "P|h1| = " + num2str( 10*log10(P*h1) ) + "[dB]" + ", P|h2| = " + num2str( 10*log10(P*h2) ) + "[dB]";
        strTitle = strTitle + " Relative Gain (Area OMA / Area NOMA) = " + num2str( tempRelativeGain ) + "[%]";
        title( strTitle )
        
        %pause(.5)

    end    

end

plot( h1_plot , relativeGain )

legend("P|h2| =" + num2str( maxh2Gain ) +  "[dB]")
ylabel("Relative Gain (NOMA/OMA) [%]")
xlabel("P|h1| [dB]" )
ylim( [ 1 , max( tempRelativeGain ) + 5 ] )

grid on
hold on