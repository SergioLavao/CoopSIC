import sys
sys.path.append("./Source")

from WirelessNetworkSolver import *

#Linear Network

distance_to_edge = 1.0 #meters
Network = HexGridNetwork( [2,2], SetRadiusFromEdge( distance_to_edge ) )
BS1 = Network.ActivateBS( 0 , 0 )
BS2 = Network.ActivateBS( 1 , 0 )

#Parameters

N_0 = 1
W = 1
rho = 1
alpha = Parameter('alpha')  
user1Distance = Parameter('d1') #User 1 distance ( from BS center to edge, in the y axis )
user2Distance = Parameter('d2') #User 1 distance ( from BS center to edge, in the y axis )
user1Position = [ 0.0, user1Distance ] #Moves along y axis
user2Position = [ 0.0, -user2Distance ] #Moves along y axis

P1 = Parameter('P1')
P2 = Parameter('P2')
BS1.SetPower( P1 )
BS2.SetPower( P2 )

''' OMA Model '''

U1 = UserOMA( BS1, 'User1', user1Position )
U2 = UserOMA( BS2, 'User2', user2Position )

print( Python2MatlabExpression( U1.GetCapacity( Network=Network, N_0=N_0, W=W, rho=1/2, alpha=alpha ) ) ) #rho = 1/2 due frequency multiplexing
print( Python2MatlabExpression( U2.GetCapacity( Network=Network, N_0=N_0, W=W, rho=1/2, alpha=alpha ) )  ) #rho = 1/2 due frequency multiplexing
Network.ClearUsers()

''' IaN '''

U1 = UserIaN( BS1, 'User1', user1Position )
U2 = UserIaN( BS2, 'User2', user2Position )

print( Python2MatlabExpression( U1.GetCapacity( Network=Network, N_0=N_0, W=W, rho=1, alpha=alpha ) ) ) #rho = 1/2 due frequency multiplexing
print( Python2MatlabExpression( U2.GetCapacity( Network=Network, N_0=N_0, W=W, rho=1, alpha=alpha ) )  ) #rho = 1/2 due frequency multiplexing
Network.ClearUsers()

''' PDM '''

BS1.SetPower( P1 )
BS2.SetPower( P2 )

U1 = UserPDM( BS1, 'User1', user1Position )
U2 = UserPDM( BS2, 'User2', user2Position )

U1.SetSICSlaves([ U2 ]) #Slave must have |h_slave|^2 <= |h_master|^2

print( Python2MatlabExpression( U1.GetCapacity( Network=Network, N_0=N_0, W=W, rho=1, alpha=alpha ) ) ) #rho = 1/2 due frequency multiplexing
print( Python2MatlabExpression( U2.GetCapacity( Network=Network, N_0=N_0, W=W, rho=1, alpha=alpha ) )  ) #rho = 1/2 due frequency multiplexing
Network.ClearUsers()

''' Cooperative SIC '''

BS1.SetPower( P1 )
BS2.SetPower( P2 )

U1 = UserCoopSIC( BS1, 'User1', user1Position )
U2 = UserCoopSIC( BS2, 'User2', user2Position )

U1.SetSICSlaves([ U2 ]) #Slave must have |h_slave|^2 <= |h_master|^2

print( Python2MatlabExpression( U1.GetCapacity( Network=Network, N_0=N_0, W=W, rho=1, alpha=alpha ) ) ) #rho = 1/2 due frequency multiplexing
print( Python2MatlabExpression( U2.GetCapacity( Network=Network, N_0=N_0, W=W, rho=1, alpha=alpha ) )  ) #rho = 1/2 due frequency multiplexing

Network.ClearUsers()

VisualizeNetwork()