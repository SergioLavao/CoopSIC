%Returns the capacity region for 2 users without power split
function CRPairUsers( P, alpha, user1RelativePosition , user2RelativePosition, plotTitle )
    
    d1x = user1RelativePosition(1);
    d1y = user1RelativePosition(2);

    d2x = user2RelativePosition(1);
    d2y = user2RelativePosition(2);

    alpha_W = 0:0.01:1;
    
    % System model
    
    User2Master = log2(1 + P./((2.0.*(0.25.*d1x.^2 + (-0.5.*d1y - 1.0).^2).^0.5).^alpha.*(P./(d1x.^2 + d1y.^2).^(0.5.*alpha) + 1.0)));
    U2Master_Internal = log2( 1 + P./(2.0.*(0.25.*d1x.^2 + (-0.5.*d1y - 1.0).^2).^0.5).^alpha );
    User1Slave = log2(1 + P./(d1x.^2 + d1y.^2).^(0.5.*alpha));
    U1Slave_Internal = log2( 1 + P./((d1x.^2 + d1y.^2).^(0.5.*alpha).*(P./(2.0.*(0.25.*d1x.^2 + (-0.5.*d1y - 1.0).^2).^0.5).^alpha + 1.0)) );

    User2Slave = log2(1 + P./(d2x.^2 + d2y.^2).^(0.5.*alpha));
    U2Slave_Internal = log2( 1 + P./((d2x.^2 + d2y.^2).^(0.5.*alpha).*(P./(2.0.*(0.25.*d2x.^2 + (1.0 - 0.5.*d2y).^2).^0.5).^alpha + 1.0)) );
    User1Master = log2(1 + P./((2.0.*(0.25.*d2x.^2 + (1.0 - 0.5.*d2y).^2).^0.5).^alpha.*(P./(d2x.^2 + d2y.^2).^(0.5.*alpha) + 1.0)));
    U1Master_Internal = log2( 1 + P./(2.0.*(0.25.*d2x.^2 + (1.0 - 0.5.*d2y).^2).^0.5).^alpha );
      
    C_OMA_User1 = (1 - alpha_W).*log2(1 + P./((1.0 - alpha_W).*(d2x.^2 + d2y.^2).^(0.5.*alpha)));
    C_OMA_User2 = (alpha_W).*log2(1 + P./(alpha_W.*(d1x.^2 + d1y.^2).^(0.5.*alpha)));
    
    C_IaN_User2 = log2(1 + P./((d2x.^2 + d2y.^2).^(0.5.*alpha).*(P./(2.0.*(0.25.*d2x.^2 + (1.0 - 0.5.*d2y).^2).^0.5).^alpha + 1.0)));
    C_IaN_User1 = log2(1 + P./((d1x.^2 + d1y.^2).^(0.5.*alpha).*(P./(2.0.*(0.25.*d1x.^2 + (-0.5.*d1y - 1.0).^2).^0.5).^alpha + 1.0)));

%     User2Master = log2(1 + 0.5.*P./((0.25.*d1x.^2 + (-0.5.*d1y - 1.0).^2).^0.5.*(P./(d1x.^2 + d1y.^2).^0.5 + 1.0)));
%     U2Master_Internal = log2( 1 + 0.5.*P./(0.25.*d1x.^2 + (-0.5.*d1y - 1.0).^2).^0.5 );
%     User1Slave = log2(1 + P./(d1x.^2 + d1y.^2).^0.5);
%     U1Slave_Internal = log2( 1 + P./((d1x.^2 + d1y.^2).^0.5.*(0.5.*P./(0.25.*d1x.^2 + (-0.5.*d1y - 1.0).^2).^0.5 + 1.0)) );

%     User2Slave = log2(1 + P./(d2x.^2 + d2y.^2).^0.5);
%     U2Slave_Internal = log2( 1 + P./((d2x.^2 + d2y.^2).^0.5.*(0.5.*P./(0.25.*d2x.^2 + (1.0 - 0.5.*d2y).^2).^0.5 + 1.0)) );
%     User1Master = log2(1 + 0.5.*P./((0.25.*d2x.^2 + (1.0 - 0.5.*d2y).^2).^0.5.*(P./(d2x.^2 + d2y.^2).^0.5 + 1.0)));
%     U1Master_Internal = log2( 1 + 0.5.*P./(0.25.*d2x.^2 + (1.0 - 0.5.*d2y).^2).^0.5 );

%     C_OMA_User1 = alpha_W.*log2(1 + P./(((d2x.^2 + d2y.^2).^0.5).*alpha_W));
%     C_OMA_User2 = (1 - alpha_W).*log2(1 + P./(((d1x.^2 + d1y.^2).^0.5).*(1 - alpha_W)));

%     C_IaN_User1 = log2(1 + P./((d2x.^2 + d2y.^2).^0.5.*(0.5.*P./(0.25.*d2x.^2 + (1.0 - 0.5.*d2y).^2).^0.5 + 1.0)));
%     C_IaN_User2 = log2(1 + P./((d1x.^2 + d1y.^2).^0.5.*(0.5.*P./(0.25.*d1x.^2 + (-0.5.*d1y - 1.0).^2).^0.5 + 1.0)));
    
    % MACS
    MAC_U1Master = [ 0 U2Slave_Internal User2Slave User2Slave ; U1Master_Internal U1Master_Internal User1Master 0 ];
    MAC_U2Master = [ 0 User2Master U2Master_Internal U2Master_Internal ; User1Slave User1Slave U1Slave_Internal 0 ];
    
    % Plots 
    plot( MAC_U1Master(1,:) , MAC_U1Master(2,:),'-o')
    hold on
    plot( MAC_U2Master(1,:) , MAC_U2Master(2,:),'-o')
    plot( C_OMA_User1 , C_OMA_User2,'-')
    plot( C_IaN_User1 , C_IaN_User2,'*')
    legend(["User1 MAC","User2 MAC","OMA MAC","IaN MAC"])
    
    ylabel('R2 [bps/Hz]')
    xlabel('R1 [bps/Hz]')

    title(plotTitle)

    MaxSROMA = max( C_OMA_User1 + C_OMA_User2 )
    MaxSRCS1 = max( MAC_U1Master(1,:) + MAC_U1Master(2,:) )
    MaxSRCS2 = max( MAC_U2Master(1,:) + MAC_U2Master(2,:) )

end