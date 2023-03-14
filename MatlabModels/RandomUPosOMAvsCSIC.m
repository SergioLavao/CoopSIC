PdB = 50;
P = 10^(PdB/10);

W = 1;
N_0 = 1;
rho = 1;
alpha = 3;

d1x= ones(1,231);
d1y= ones(1,231);
d2x= ones(1,231);
d2y= ones(1,231);
d3x= ones(1,231);
d3y= ones(1,231);

dx = -1.15:0.01:1.15;
dy = -1:0.00869:1;

hexagon_vertices = [-1.15, 0; -0.57, 1; 0.57, 1; 1.15, 0; 0.57, -1; -0.57, -1];

c = 0;
[MaxCapOMAOCI, MaxCapCoopSICOCI, MaxCapIaN ] = deal(NaN*ones(1,c)); 

for i = 1 : 1 : 1000

    d1x(i) = dx(randi([1, 231]));
    d1y(i) = dx(randi([1, 231]));
    
    d2x(i) = dx(randi([1, 231]));
    d2y(i) = dx(randi([1, 231]));

    d3x(i) = dx(randi([1, 231]));
    d3y(i) = dx(randi([1, 231]));

    if inpolygon(d1x(i), d1y(i), hexagon_vertices(:,1), hexagon_vertices(:,2)) && inpolygon(d2x(i), d2y(i), hexagon_vertices(:,1), hexagon_vertices(:,2)) && inpolygon(d3x(i), d3y(i), hexagon_vertices(:,1), hexagon_vertices(:,2))

        c = c + 1;
        MaxCapOMAOCI(i) = OCIOptimalOMAN( P,W,N_0,alpha,d1x(i),d1y(i),d2x(i),d2y(i),d3x(i),d3y(i));
        MaxCapCoopSICOCI(i) = OCIPermCoopSICN2N3(P,W,rho,N_0,alpha,d1x(i),d1y(i),d2x(i),d2y(i),d3x(i),d3y(i));
        MaxCapIaN(i) = IaNModel( P,W,N_0,alpha,d1x(i),d1y(i),d2x(i),d2y(i),d3x(i),d3y(i) );

    else

        d1x(i) = NaN;
        d1y(i) = NaN;

        d2x(i) = NaN;
        d2y(i) = NaN;

        d3x(i) = NaN;
        d3y(i) = NaN;

    end

end 

meanOMA = mean(MaxCapOMAOCI)
meanCoopSIC = mean(MaxCapCoopSICOCI)
meanIaN = mean( MaxCapIaN )

plot( d1x,d1y , "*","Color","r")

hold on

plot( d2x - 1.72,d2y + 1, "x","Color","g")

hold on

plot( d3x,d3y + 2, "+","Color","b")

hold on

plot( polyshape(hexagon_vertices) )

plot( polyshape([ hexagon_vertices(:,1) - 1.72, hexagon_vertices(:,2) + 1]) )

plot( polyshape([ hexagon_vertices(:,1), hexagon_vertices(:,2) + 2]) )

ylim([-1.5,3.5])
xlim([-3.2,1.8])
