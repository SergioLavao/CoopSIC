P_dB = -10;
P = 10^(P_dB/10);

alpha = 3;

d2x = -0.57:0.01:0.57;

C_CoopSIC_User1 = log2(1 + P);

C_CoopSIC_User2_Eq1 = log2(1 + P./(P + 1.0)) + zeros( size(d2x) ); %Master outage limit

User2_SINR = P.*sqrt(d2x.^2 + 1).^-alpha./(P.*sqrt(d2x.^2 + 1).^-alpha + 1);
C_CoopSIC_User2_Eq2 = log2(1 + User2_SINR); %Slave outage limit

SR_CoopSIC = C_CoopSIC_User1 + min( [ C_CoopSIC_User2_Eq1; C_CoopSIC_User2_Eq2 ] );

SR_OMA = 1/2*log2( 1 + 2*P ) + 1/2*log2( 1 + 2 * P * sqrt(d2x.^2 + 1).^-alpha );

%
C_CoopSIC_User2 = log2(1 + P./(1.15.*P + 1.0));
C_CoopSIC_User1 = log2(1 + P./(2.15.*P + 1.0));
CoopSIC = C_CoopSIC_User2+C_CoopSIC_User1
C_OMA_User2 = (0.25).*log2(1 + P./(1.15.*P + 0.25));
C_OMA_User1 = (0.25).*log2(1 + P./(1.15.*P + 0.25));
OMA = C_OMA_User2+C_OMA_User1


plot( d2x , ( ( SR_CoopSIC ./ SR_OMA) - 1 ) * 100 )
xlabel(" User 2 distance[Normalized] ")
ylabel(" Relative gain CoopSIC / OMA [%]")