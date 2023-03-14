%function [ PDMCapacity ] = PDMTrisec( P, W,rho,N_0,alpha,d1x,d1y,d2x,d2y,d3x,d3y)

alpha = 3;

d1y = -1;
d1x = -0.577;
d2y = 1;
d2x = -0.577;
d3y = 0;
d3x = 1.1547;

H_11 = (d1x.^2 + d1y.^2).^(-0.5.*alpha);
H_21 = (2.0.*(0.25.*d1x.^2 + (-0.5.*d1y - 1.0).^2).^0.5).^(-alpha);
H_31 = (1.73.*((-0.577.*d1x - 1.0).^2 + 0.333.*(-d1y - 1.0).^2).^0.5).^(-alpha);
H_12 = (2.0.*(0.25.*d2x.^2 + (1.0 - 0.5.*d2y).^2).^0.5).^(-alpha);
H_22 = (d2x.^2 + d2y.^2).^(-0.5.*alpha);
H_32 = (1.73.*(0.333.*(1.0 - d2y).^2 + (-0.577.*d2x - 1.0).^2).^0.5).^(-alpha);
H_13 = (1.73.*((1.0 - 0.577.*d3x).^2 + 0.333.*(1.0 - d3y).^2).^0.5).^(-alpha);
H_23 = (1.73.*((1.0 - 0.577.*d3x).^2 + 0.333.*(-d3y - 1.0).^2).^0.5).^(-alpha);
H_33 = (d3x.^2 + d3y.^2).^(-0.5.*alpha);

alias = ["h_11" "h_22" "h_33" "h_21" "h_12" "h_23" "h_31" "h_32" "h_13"];
initial_order = [H_11, H_22, H_33, H_21, H_12, H_23, H_31, H_32, H_13];

[itself_order, I_it] = sort( initial_order(1:3) , "descend" );
[sorted, I] = sort( initial_order , "descend" );

itself_order;
itself_string = "";

for i = 1:numel(I_it)
    itself_string = itself_string + " " + alias(I_it(i)) + " > " ;
end

itself_string

sorted;
string = "";
for i = 1:numel(I)
    sorted()
    string = string + " " + alias(I(i)) + " > " ;
end

string 
%end