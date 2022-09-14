import sys
sys.path.append("./Source")

from WirelessNetworkSolver import *

Network = HexGridNetwork( [2,2], SetRadiusFromEdge( 1 ) )

'''Noise , BW and Reuse factor parameters '''
N_0 = 1
W = 1
rho = 1

BS1 = Network.ActivateBS( 0 , 0 )
BS2 = Network.ActivateBS( 1 , 0 )

P1 = 1#dB
P2 = 100#dB


BS1.SetPower( P1 )
BS2.SetPower( P2 )

U1 = UserOMA( BS1, 'User1', [0.0,1.0] )
U2 = UserOMA( BS2, 'User2', [0.0,-1.0] )

alpha = Parameter('alpha')

print( Python2MatlabExpression( U1.GetCapacity( Network, N_0, W, alpha, 3 ) ) )
print( Python2MatlabExpression( U2.GetCapacity( Network, N_0, W, (1-alpha), 3 ) )  )

Network.ClearUsers()

U1 = UserPDM( BS1, 'User1', [0.0,1.0] )
U2 = UserPDM( BS2, 'User2', [0.0,-1.0] )

U2.SetSICSlaves([ U1 ])

BS1.SetPower( P1 )
BS2.SetPower( P2 )

print( Python2MatlabExpression( U1.GetCapacity( Network, N_0, W, rho, 3 ) ) )
print( Python2MatlabExpression( U2.GetCapacity( Network, N_0, W, rho, 3 ) )  )

Network.ClearUsers()

U1 = UserCoopSIC( BS1, 'User1', [0.0,1.0] )
U2 = UserCoopSIC( BS2, 'User2', [0.0,-1.0] )

U2.SetSICSlaves([ U1 ])

BS1.SetPower( P1 )
BS2.SetPower( P2 )

print( Python2MatlabExpression( U1.GetCapacity( Network, N_0, W, rho, 3 ) ) )
print( Python2MatlabExpression( U2.GetCapacity( Network, N_0, W, rho, 3 ) ) )

Network.ClearUsers()

U1 = UserIaN( BS1, 'User1', [0.0,1.0] )
U2 = UserIaN( BS2, 'User2', [0.0,-1.0] )

BS1.SetPower( P1 )
BS2.SetPower( P2 )

print( Python2MatlabExpression( U1.GetCapacity( Network, N_0, W, rho, 3 ) ) )
print( Python2MatlabExpression( U2.GetCapacity( Network, N_0, W, rho, 3 ) ) )

VisualizeNetwork()