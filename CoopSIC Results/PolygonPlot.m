figure

L = linspace(0,2*pi,7); %Cracks
xv = cos(L)';
yv = sin(L)';

xq = randn(250,1);
yq = randn(250,1);

in = inpolygon(xq,yq,xv,yv);

plot(xv,yv)
axis equal

hold on
plot(xq(in),yq(in),'r+') 

hold off