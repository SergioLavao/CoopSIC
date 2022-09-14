import sys
sys.path.append("./Source")

from WirelessNetworkSolver import *

''' Comparison between models OMA(rho=1/2), PDM(PF=1/2), IaN and CoopSIC changing user parameters in TX-RX pair'''
distance_to_edge = 1.0 #meters

Network = HexGridNetwork( [2,2], SetRadiusFromEdge( distance_to_edge ) )

'''Noise , BW and Reuse factor parameters (Normalized!)'''
alpha = Parameter('alpha')
N_0 = Parameter('N_0')
rho = 1
W = 1

P1 = Parameters('P1') #Base station power 
P2 = Parameters('P2') #Base station power 
BS1 = Network.ActivateBS( 0 , 0 )
BS2 = Network.ActivateBS( 1 , 0 )

user_1_position = [0.0,Parameter('d')]

''' OMA Model '''
BS1.SetPower( P1 )
BS2.SetPower( P2 )

U1 = UserOMA( BS1, 'User1', user_1_position )
U2 = UserOMA( BS2, 'User2', [0.0,-distance_to_edge] )

print( Python2MatlabExpression( U1.GetCapacity( Network=Network, N_0=N_0, W=W, rho=1/2, alpha=alpha ) ) )
print( Python2MatlabExpression( U2.GetCapacity( Network=Network, N_0=N_0, W=W, rho=1/2, alpha=alpha ) )  )
Network.ClearUsers()

''' IaN Model '''
BS1.SetPower( P1 )
BS2.SetPower( P2 )

U1 = UserIaN( BS1, 'User1', user_1_position )
U2 = UserIaN( BS2, 'User2', [0.0,-distance_to_edge] )

print( Python2MatlabExpression( U1.GetCapacity( Network=Network, N_0=N_0, W=W, rho=rho, alpha=alpha ) ) )
print( Python2MatlabExpression( U2.GetCapacity( Network=Network, N_0=N_0, W=W, rho=rho, alpha=alpha ) )  )
Network.ClearUsers()

''' PDM Model PF=1/2'''
PF = 1/2

BS1.SetPower( P1*PF )
BS2.SetPower( P2*PF )

U1 = UserPDM( BS1, 'User1', user_1_position )
U2 = UserPDM( BS2, 'User2', [0.0,-distance_to_edge] )

U1.SetSICSlaves([ U2 ]) #Slave must have |h_slave|^2 <= |h_master|^2

print( Python2MatlabExpression( U1.GetCapacity( Network=Network, N_0=N_0, W=W, rho=rho, alpha=alpha ) ) )
print( Python2MatlabExpression( U2.GetCapacity( Network=Network, N_0=N_0, W=W, rho=rho, alpha=alpha ) )  )
Network.ClearUsers()

''' CoopSIC Model'''
BS1.SetPower( P1 )
BS2.SetPower( P2 )

U1 = UserCoopSIC( BS1, 'User1', user_1_position )
U2 = UserCoopSIC( BS2, 'User2', [0.0,-distance_to_edge] )

U1.SetSICSlaves([ U2 ]) #Slave must have |h_slave|^2 <= |h_master|^2

print( Python2MatlabExpression( U1.GetCapacity( Network=Network, N_0=N_0, W=W, rho=rho, alpha=alpha ) ) )
print( Python2MatlabExpression( U2.GetCapacity( Network=Network, N_0=N_0, W=W, rho=rho, alpha=alpha ) )  )
Network.ClearUsers()

VisualizeNetwork()