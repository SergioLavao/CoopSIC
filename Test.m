
% Corner Points MAC 1

User1_Internal = log2( 1 + 0.476 );
User1 = log2(1 + 0.226); %User 1 Slave 

User2_Internal = log2( 1 + 0.748 );
User2 = log2(1 + 1.10); % User 2 Master

MAC1 = [ 0 User1 User1_Internal User1_Internal ; User2 User2 User2_Internal 0 ];

%Corner Points MAC 2

User1_Internal = log2( 1 + 0.602 );
User1 = log2(1 + 1.11); % USer 1 Master

User2_Internal = log2( 1 + 0.841 );
User2 = log2(1 + 0.399); % User 2 Slave

MAC2 = [ 0 User1_Internal User1 User1 ; User2_Internal User2_Internal User2 0 ];

% MAC OMA

alpha = 0:0.01:1;

OMA_User1 = alpha.*log2( 1 + 1.11./alpha );
OMA_User2 = (1 - alpha).*log2( 1 + 1.11./(1 - alpha) );

OMA_User1_x = 0.5*log2( 1 + 2*1.11 );
OMA_User2_x = 0.5.*log2( 1 + 2*1.11 );

% MAC IaN

C_IaN_User1 = log2(1 + 0.602);
C_IaN_User2 = log2(1 + 0.748);

plot( MAC1(1,:) , MAC1(2,:),'-o')
hold on
plot( MAC2(1,:) , MAC2(2,:),'-o')
plot( C_IaN_User1 , C_IaN_User2,'*')
plot( OMA_User1_x , OMA_User2_x,'*')
plot( OMA_User1 , OMA_User2,'-')

ylabel('R2')
xlabel('R1')