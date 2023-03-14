PdB = 50;
P = 10^(PdB/10);

W = 1;
N_0 = 1;
rho = 1;
alpha = 3;

offset = 0:0.01:1

d1y = -1 + offset;
d1x = -0.577 - 0.577*offset;

d2y = 1*ones(size(offset));
d2x = offset*1.154 - 0.577; 

d3y = offset;
d3x = 1.154 - 0.577*offset;

plot( d1x,d1y )
xlim([-5,5])
ylim([-5,5])

c = 0;
[MaxCapOMA, MaxCapCoopSIC, i_x ] = deal(NaN*ones(1,c)); 

for i = 1 : 1 : 101
    c = c + 1;
    MaxCapOMA(i) = OptimalOMAN( P ,W,N_0,alpha,d1x(i),d1y(i),d2x(i),d2y(i),d3x(i),d3y(i));
    [MaxCapCoopSIC(i), i_x(i)] = PermutationCoopSIC( P, W,rho,N_0,alpha,d1x(i),d1y(i),d2x(i),d2y(i),d3x(i),d3y(i));
end

plot( offset , MaxCapOMA )
hold on
plot( offset , MaxCapCoopSIC )