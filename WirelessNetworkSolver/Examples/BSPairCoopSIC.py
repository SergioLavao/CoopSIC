import sys
sys.path.append("../Source")

from WirelessNetworkSolver import *

W = 1
rho = 1
N_0 = 1
alpha = 1
P = 1

distance_to_edge = 1.0
Network = HexGridNetwork( [2,2], SetRadiusFromEdge( distance_to_edge ) )
Network.SetNetworkParameters( W, rho, N_0, alpha, P )

Editor = NetworkEditor( Network )

BS1 = Network.ActivateBS( 1 , 0, 'BS1' )
BS2 = Network.ActivateBS( 0 , 0, 'BS2' )

BS1.SetPower( P )
BS2.SetPower( P )

d1y = -1.0;
d1x = 0.0;

d2y = 1.0;
d2x = 0.0;

U1 = UserCoopSIC( BS1, 'User1', [d1x,d1y] )
U2 = UserCoopSIC( BS2, 'User2', [d2x,d2y] )

U1.SetSICSlaves([ U2 ])

Editor.AddNetworkModel('CoopSIC')

U1 = UserOMA( BS1, 'User1', [d1x,d1y] )
U1.SetOMAParameters( 1/2,1 )
U2 = UserOMA( BS2, 'User2', [d2x,d2y]  )
U2.SetOMAParameters( 1/2,1 )

Editor.AddNetworkModel('OMA')

U1 = UserIaN( BS1, 'User1', [d1x,d1y] )
U2 = UserIaN( BS2, 'User2', [d2x,d2y]  )

Editor.AddNetworkModel('IaN')

VisualizeNetwork()