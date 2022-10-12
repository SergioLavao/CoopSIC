import sys
sys.path.append("./Source")

from WirelessNetworkSolver import *

#Linear Network

distanceToEdge = 1.0
distanceToCorner = SetRadiusFromEdge( distanceToEdge )

Network = HexGridNetwork( [4,4], distanceToCorner )
Network.SetNetworkParameters( 1, 1, 1, 3,Parameter('P') )

U1Position = [0.0,1.0]
U2Position = [0.0,-1.0]

Editor = NetworkEditor( Network )

BS1 = Network.ActivateBS( 1 , 1, 'BS1' )
BS2 = Network.ActivateBS( 2 , 1, 'BS2' )

U1 = UserCoopSIC( BS1, 'User1', U1Position )
U2 = UserCoopSIC( BS2, 'User2', U2Position )
U1.SetSICSlaves( [ U2 ] )

Editor.AddNetworkModel('Coop_SIC_Network')

alpha = 1/2

U1 = UserOMA( BS1, 'User1', U1Position )
U2 = UserOMA( BS2, 'User2', U2Position )

U1.SetAlpha( alpha )
U2.SetAlpha( alpha )

Editor.AddNetworkModel('OMA_Network')

VisualizeNetwork()