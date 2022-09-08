import sys
sys.path.append("../Source")

from WirelessNetworkSolver import *

Network = HexGridNetwork( [5,5], SetRadiusFromEdge( 1 ) )

P = Parameter('P')
beta = Parameter('beta')

N_0, W, rho, alpha = Parameters('N_0 W rho alpha')