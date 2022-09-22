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
alpha = 3  
user1Distance = Parameter('d1') #User 1 distance ( from BS center to edge, in the y axis )
user2Distance = Parameter('d2') #User 1 distance ( from BS center to edge, in the y axis )
user2Distance = 1.0
user1Position = [ 0.0, user1Distance ] #Moves along y axis
user2Position = [ 0.0, -user2Distance ] #Moves along y axis

epsilon = Parameter('epsilon')
P = Parameter('P')
P1 = epsilon*P
P2 = (1 - epsilon)*P
BS1.SetPower( P1 )
BS2.SetPower( P2 )

''' Coop SIC Model '''

U1 = UserCoopSIC( BS1, 'User1', user1Position )
U2 = UserCoopSIC( BS2, 'User2', user2Position )

U1.SetSICSlaves([ U2 ]) #Slave must have |h_slave|^2 <= |h_master|^2

U1.GetSINR( Network, N_0, W, rho, alpha )
U2.GetSINR( Network, N_0, W, rho, alpha )

CoopSICLimit = U1.sinr

Network.ClearUsers()

''' PDM Model '''

U1 = UserPDM( BS1, 'User1', user1Position )
U2 = UserPDM( BS2, 'User2', user2Position )

U1.SetSICSlaves([ U2 ]) #Slave must have |h_slave|^2 <= |h_master|^2

U1.GetSINR( Network, N_0, W, rho, alpha )
U2.GetSINR( Network, N_0, W, rho, alpha )

PDMLimit = U2.sinr

print( CoopSICLimit )
print( PDMLimit )

Network.ClearUsers()
