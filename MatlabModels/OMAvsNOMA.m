%Variable Channel gains comparison OMA vs NOMA

%   OMA 

P = 1; %Normalized Power

h1_ = 0; %dB
h2_ = 10; %dB

h1 = 10^(h1_/10);
h2 = 10^(h2_/10);

OMASamples = 100; %Number of points on OMA plot
[R1_OMA , R2_OMA] = OptimalOMA( P, h1, h2, OMASamples, true ); %Params = Power, gain1, gain2, #samples, b_plot

%   NOMA

beta = 0:0.01:1; % Power split vector

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