import sys
sys.path.append("./Source")

from WirelessNetworkSolver import *

#Linear Network

distance_to_edge = 1.0
Network = HexGridNetwork( [2,2], SetRadiusFromEdge( distance_to_edge ) )
Network.SetNetworkParameters( Parameter('W'), Parameter('rho'), Parameter('N_0'), Parameter('alpha') )

BS1 = Network.ActivateBS( 0 , 0, 'BS1' )
BS2 = Network.ActivateBS( 1 , 0, 'BS2' )

BS1.SetPower( Parameter('P1') )
BS2.SetPower( Parameter('P2') )

U1 = UserCoopSIC( BS1, 'User1', [0.0,1.0] )
U2 = UserCoopSIC( BS2, 'User2', [0.0,-1.0] )
U1.SetSICSlaves([ U2 ]) #Slave must have |h_slave|^2 <= |h_master|^2

Editor = NetworkEditor( Network )

VisualizeNetwork()