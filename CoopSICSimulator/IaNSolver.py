import sys
sys.path.append("./Source")

from WirelessNetworkSolver import *

Network = HexGridNetwork( [5,5], SetRadiusFromEdge( 1 ) )

'''Noise , BW and Reuse factor parameters '''
N_0, W, rho, alpha = Parameters('N_0 W rho alpha')

BS1 = Network.ActivateBS( 0 , 0 )
BS2 = Network.ActivateBS( 1 , 0 )

P = Parameter('P')
BS1.SetPower( P )
BS2.SetPower( P )

U1 = UserIaN( BS1, 'User1', [0.0,Parameter('d1')] )
U2 = UserIaN( BS2, 'User2', [0.0,-1.0] )

print( Python2MatlabExpression( U1.GetSINR( Network, N_0, W, rho, alpha ) ) )
print( Python2MatlabExpression( U2.GetSINR( Network, N_0, W, rho, alpha ) )  )

VisualizeNetwork()