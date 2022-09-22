import sys
sys.path.append("./Source")

from WirelessNetworkSolver import *

alpha = Parameter('alpha')  
d1 = Parameter('d1') #User 1 distance ( from BS center to edge, in the y axis )
d1 = Parameter('d2') #User 1 distance ( from BS center to edge, in the y axis )

P1 = Parameter('P1')
P2 = Parameter('P2')

def log2( expression ):
	return sym.log(expression,2)

C_PDM_User1 = log2(1 + 0.5*P1/(d1^2)^(0.5*alpha));

#Variable distance
print(sym.latex(C_PDM_User1))
