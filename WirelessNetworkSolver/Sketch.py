import sys
sys.path.append("../Source")

from WirelessNetworkSolver import *

P = Parameter('P')
beta = Parameter('beta')

P_1 = Parameter('P1')
P_2 = Parameter('P2')

N_0, W, rho, alpha = Parameters('N_0 W rho alpha')

edge_distance = 1
radius = SetRadiusFromEdge( edge_distance ) 

Network = HexGridNetwork( [5,5], radius )
Editor = NetworkEditor( Network )

ActivateTrisec( Network, 1 , 1 )

ActivateTrisec( Network, 3 , 2 )

ActivateTrisec( Network, 3 , 0 )

VisualizeNetwork()
