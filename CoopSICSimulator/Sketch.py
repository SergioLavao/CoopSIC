import sys
sys.path.append("./Source")

from WirelessNetworkSolver import *

P = Parameter('P')
beta = Parameter('beta')

P_1 = Parameter('P1')
P_2 = Parameter('P2')

N_0, W, rho, alpha = Parameters('N_0 W rho alpha')

edge_distance = 1
radius = SetRadiusFromEdge( edge_distance ) 

Network = HexGridNetwork( [2,2], radius )

BS1 = Network.ActivateBS( 0 , 0 )
BS2 = Network.ActivateBS( 1 , 0 )

BS1.SetPower( P_1 )
BS2.SetPower( P_2 )

U1 = UserCoopSIC( BS1, 'User1', [0.0,Parameter('d1')] )
U2 = UserCoopSIC( BS2, 'User2', [0.0,-1.0] )

U1.SetSICSlaves( [ U2 ] )

print( Python2MatlabExpression( U1.GetSINR( Network, N_0, W, rho, alpha ) ) )
print( Python2MatlabExpression( U2.GetSINR( Network, N_0, W, rho, alpha ) )  )

VisualizeNetwork()