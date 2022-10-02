%Comparison between OMA(OFDM) vs NOMA(PDM)
%OFDM Must use power split P = P1 + P2. Same as PDM

filename = 'OMAvsNOMA.gif';

%Alpha optimization to compute the boundary on OMA
for alpha = 0.01 : 0.01 : 1

beta = 0:0.01:1;

P = 1;
P_1 = beta*P*1;
P_2 = (1 - beta)*P*100;

%Alpha optimization to compute the boundary on OMA
R1_OMA = alpha.*log2(1 + P_1./alpha);
R2_OMA = (1 - alpha).*log2(1 + P_2./(1 - alpha));

R1_NOMA = log2(1 + P_1);
R2_NOMA = log2(1 + P_2./(1 + P_1));

plot(R1_OMA,R2_OMA)
hold on
plot(R1_NOMA,R2_NOMA)
hold on
grid on

legend('OMA','NOMA')
xlabel('Capacity User 1')
ylabel('Capacity User 2')

drawnow

%// Capture frame to write to gif.
frame = getframe(1);
im = frame2im(frame);
[imind,cm] = rgb2ind(im,256);
if alpha == 0.01
    imwrite(imind,cm,filename,'gif', 'Loopcount',inf);
else
    imwrite(imind,cm,filename,'gif','WriteMode','append');
end

pause(.05)

clf


end