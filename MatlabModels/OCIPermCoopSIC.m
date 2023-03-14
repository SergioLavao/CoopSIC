function [ CoopSICCapOCI, i_x] = OCIPermCoopSIC(P,W,rho,N_0,alpha,d1x,d1y,d2x,d2y,d3x,d3y)
% with 3 cell interference

% 1 -> User1 -> User2 , User3
% 2 -> User1 -> User3 , User2
% 3 -> User2 -> User1 , User3
% 4 -> User2 -> User3 , User1
% 5 -> User3 -> User1 , User2
% 6 -> User3 -> User2 , User1

% Permutation  User1 -> User2 , User3
C_CoopSIC_User3 = (W.*rho).*log2(1 + P./((d3x.^2 + d3y.^2).^(0.5.*alpha).*(N_0.*W.*rho + P./(1.73.*((1.0 - 0.577.*d3x).^2 + 0.333.*(-d3y - 1.0).^2).^0.5).^alpha + P./(1.73.*((1.0 - 0.577.*d3x).^2 + 0.333.*(1.0 - d3y).^2).^0.5).^alpha)));
C_CoopSIC_User2 = (W.*rho).*log2(1 + P./((d2x.^2 + d2y.^2).^(0.5.*alpha).*(N_0.*W.*rho + P./(2.0.*(0.25.*d2x.^2 + (1.0 - 0.5.*d2y).^2).^0.5).^alpha + P./(1.73.*(0.333.*(1.0 - d2y).^2 + (-0.577.*d2x - 1.0).^2).^0.5).^alpha)));
C_CoopSIC_User1 = (W.*rho).*log2(1 + P./((d1x.^2 + d1y.^2).^(0.5.*alpha).*(N_0.*W.*rho + P./(3.0.*(0.333.*(-0.577.*d1x - 1.0).^2 + (-0.333.*d1y - 1.0).^2).^0.5).^alpha + P./(1.73.*(0.333.*(1.0 - d1y).^2 + (-0.577.*d1x - 1.0).^2).^0.5).^alpha + P./(1.73.*((1.0 - 0.577.*d1x).^2 + 0.333.*(-d1y - 1.0).^2).^0.5).^alpha)));
CoopSICUser1_User2User3 = C_CoopSIC_User3+C_CoopSIC_User2+C_CoopSIC_User1;
 % Permutation  User1 -> User3 , User2
C_CoopSIC_User3 = (W.*rho).*log2(1 + P./((d3x.^2 + d3y.^2).^(0.5.*alpha).*(N_0.*W.*rho + P./(1.73.*((1.0 - 0.577.*d3x).^2 + 0.333.*(-d3y - 1.0).^2).^0.5).^alpha + P./(1.73.*((1.0 - 0.577.*d3x).^2 + 0.333.*(1.0 - d3y).^2).^0.5).^alpha)));
C_CoopSIC_User2 = (W.*rho).*log2(1 + P./((d2x.^2 + d2y.^2).^(0.5.*alpha).*(N_0.*W.*rho + P./(2.0.*(0.25.*d2x.^2 + (1.0 - 0.5.*d2y).^2).^0.5).^alpha + P./(1.73.*(0.333.*(1.0 - d2y).^2 + (-0.577.*d2x - 1.0).^2).^0.5).^alpha)));
C_CoopSIC_User1 = (W.*rho).*log2(1 + P./((d1x.^2 + d1y.^2).^(0.5.*alpha).*(N_0.*W.*rho + P./(3.0.*(0.333.*(-0.577.*d1x - 1.0).^2 + (-0.333.*d1y - 1.0).^2).^0.5).^alpha + P./(1.73.*(0.333.*(1.0 - d1y).^2 + (-0.577.*d1x - 1.0).^2).^0.5).^alpha + P./(1.73.*((1.0 - 0.577.*d1x).^2 + 0.333.*(-d1y - 1.0).^2).^0.5).^alpha)));
CoopSICUser1_User3User2 = C_CoopSIC_User3+C_CoopSIC_User2+C_CoopSIC_User1;
 % Permutation  User2 -> User1 , User3
C_CoopSIC_User3 = (W.*rho).*log2(1 + P./((d3x.^2 + d3y.^2).^(0.5.*alpha).*(N_0.*W.*rho + P./(1.73.*((1.0 - 0.577.*d3x).^2 + 0.333.*(-d3y - 1.0).^2).^0.5).^alpha + P./(1.73.*((1.0 - 0.577.*d3x).^2 + 0.333.*(1.0 - d3y).^2).^0.5).^alpha)));
C_CoopSIC_User2 = (W.*rho).*log2(1 + P./((d2x.^2 + d2y.^2).^(0.5.*alpha).*(N_0.*W.*rho + P./(3.0.*((1.0 - 0.333.*d2y).^2 + 0.333.*(-0.577.*d2x - 1.0).^2).^0.5).^alpha + P./(1.73.*((-0.577.*d2x - 1.0).^2 + 0.333.*(-d2y - 1.0).^2).^0.5).^alpha + P./(1.73.*((1.0 - 0.577.*d2x).^2 + 0.333.*(1.0 - d2y).^2).^0.5).^alpha)));
C_CoopSIC_User1 = (W.*rho).*log2(1 + P./((d1x.^2 + d1y.^2).^(0.5.*alpha).*(N_0.*W.*rho + P./(2.0.*(0.25.*d1x.^2 + (-0.5.*d1y - 1.0).^2).^0.5).^alpha + P./(1.73.*((-0.577.*d1x - 1.0).^2 + 0.333.*(-d1y - 1.0).^2).^0.5).^alpha)));
CoopSICUser2_User1User3 = C_CoopSIC_User3+C_CoopSIC_User2+C_CoopSIC_User1;
 % Permutation  User2 -> User3 , User1
C_CoopSIC_User3 = (W.*rho).*log2(1 + P./((d3x.^2 + d3y.^2).^(0.5.*alpha).*(N_0.*W.*rho + P./(1.73.*((1.0 - 0.577.*d3x).^2 + 0.333.*(-d3y - 1.0).^2).^0.5).^alpha + P./(1.73.*((1.0 - 0.577.*d3x).^2 + 0.333.*(1.0 - d3y).^2).^0.5).^alpha)));
C_CoopSIC_User2 = (W.*rho).*log2(1 + P./((d2x.^2 + d2y.^2).^(0.5.*alpha).*(N_0.*W.*rho + P./(3.0.*((1.0 - 0.333.*d2y).^2 + 0.333.*(-0.577.*d2x - 1.0).^2).^0.5).^alpha + P./(1.73.*((-0.577.*d2x - 1.0).^2 + 0.333.*(-d2y - 1.0).^2).^0.5).^alpha + P./(1.73.*((1.0 - 0.577.*d2x).^2 + 0.333.*(1.0 - d2y).^2).^0.5).^alpha)));
C_CoopSIC_User1 = (W.*rho).*log2(1 + P./((d1x.^2 + d1y.^2).^(0.5.*alpha).*(N_0.*W.*rho + P./(2.0.*(0.25.*d1x.^2 + (-0.5.*d1y - 1.0).^2).^0.5).^alpha + P./(1.73.*((-0.577.*d1x - 1.0).^2 + 0.333.*(-d1y - 1.0).^2).^0.5).^alpha)));
CoopSICUser2_User3User1 = C_CoopSIC_User3+C_CoopSIC_User2+C_CoopSIC_User1;
 % Permutation  User3 -> User1 , User2
C_CoopSIC_User3 = (W.*rho).*log2(1 + P./((d3x.^2 + d3y.^2).^(0.5.*alpha).*(N_0.*W.*rho + P./(3.46.*(0.0833.*d3y.^2 + (1.0 - 0.289.*d3x).^2).^0.5).^alpha + P./(2.0.*(0.25.*d3x.^2 + (-0.5.*d3y - 1.0).^2).^0.5).^alpha + P./(2.0.*(0.25.*d3x.^2 + (1.0 - 0.5.*d3y).^2).^0.5).^alpha)));
C_CoopSIC_User2 = (W.*rho).*log2(1 + P./((d2x.^2 + d2y.^2).^(0.5.*alpha).*(N_0.*W.*rho + P./(2.0.*(0.25.*d2x.^2 + (1.0 - 0.5.*d2y).^2).^0.5).^alpha + P./(1.73.*(0.333.*(1.0 - d2y).^2 + (-0.577.*d2x - 1.0).^2).^0.5).^alpha)));
C_CoopSIC_User1 = (W.*rho).*log2(1 + P./((d1x.^2 + d1y.^2).^(0.5.*alpha).*(N_0.*W.*rho + P./(2.0.*(0.25.*d1x.^2 + (-0.5.*d1y - 1.0).^2).^0.5).^alpha + P./(1.73.*((-0.577.*d1x - 1.0).^2 + 0.333.*(-d1y - 1.0).^2).^0.5).^alpha)));
CoopSICUser3_User1User2 = C_CoopSIC_User3+C_CoopSIC_User2+C_CoopSIC_User1;
 % Permutation  User3 -> User2 , User1
C_CoopSIC_User3 = (W.*rho).*log2(1 + P./((d3x.^2 + d3y.^2).^(0.5.*alpha).*(N_0.*W.*rho + P./(3.46.*(0.0833.*d3y.^2 + (1.0 - 0.289.*d3x).^2).^0.5).^alpha + P./(2.0.*(0.25.*d3x.^2 + (-0.5.*d3y - 1.0).^2).^0.5).^alpha + P./(2.0.*(0.25.*d3x.^2 + (1.0 - 0.5.*d3y).^2).^0.5).^alpha)));
C_CoopSIC_User2 = (W.*rho).*log2(1 + P./((d2x.^2 + d2y.^2).^(0.5.*alpha).*(N_0.*W.*rho + P./(2.0.*(0.25.*d2x.^2 + (1.0 - 0.5.*d2y).^2).^0.5).^alpha + P./(1.73.*(0.333.*(1.0 - d2y).^2 + (-0.577.*d2x - 1.0).^2).^0.5).^alpha)));
C_CoopSIC_User1 = (W.*rho).*log2(1 + P./((d1x.^2 + d1y.^2).^(0.5.*alpha).*(N_0.*W.*rho + P./(2.0.*(0.25.*d1x.^2 + (-0.5.*d1y - 1.0).^2).^0.5).^alpha + P./(1.73.*((-0.577.*d1x - 1.0).^2 + 0.333.*(-d1y - 1.0).^2).^0.5).^alpha)));
CoopSICUser3_User2User1 = C_CoopSIC_User3+C_CoopSIC_User2+C_CoopSIC_User1;

[CoopSICCapOCI, i_x] = max( [ CoopSICUser1_User2User3 , CoopSICUser1_User3User2 , CoopSICUser2_User1User3 , CoopSICUser2_User3User1 , CoopSICUser3_User1User2 , CoopSICUser3_User2User1  ]) ;

end