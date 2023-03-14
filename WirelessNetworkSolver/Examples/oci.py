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

Network = HexGridNetwork( [8,8], radius )
Editor = NetworkEditor( Network )

BS1 = Network.ActivateBS( 5 , 1, 'BS1' )
BS2 = Network.ActivateBS( 4 , 1, 'BS4' )
BS3 = Network.ActivateBS( 3 , 1, 'BS5' )
BS4 = Network.ActivateBS( 2 , 1, 'BS6' )

BS5 = Network.ActivateBS( 6 , 2, 'BS2' )
BS6 = Network.ActivateBS( 5 , 2, 'BS2' )
BS7 = Network.ActivateBS( 4 , 2, 'BS2' )
BS8 = Network.ActivateBS( 3 , 2, 'BS2' )
BS9 = Network.ActivateBS( 2 , 2, 'BS2' )



BS10 = Network.ActivateBS( 6 , 3, 'BS3' )
BS11= Network.ActivateBS( 5 , 3, 'BS3' )
BS12 = Network.ActivateBS( 4 , 3, 'BS3' )
BS13 = Network.ActivateBS( 3 , 3, 'BS3' )
BS14 = Network.ActivateBS( 2 , 3, 'BS3' )
BS15 = Network.ActivateBS( 1 , 3, 'BS3' )

BS2 = Network.ActivateBS( 6 , 4, 'BS2' )
BS2 = Network.ActivateBS( 5 , 4, 'BS2' )
BS2 = Network.ActivateBS( 4 , 4, 'BS2' )
BS2 = Network.ActivateBS( 3 , 4, 'BS2' )
BS2 = Network.ActivateBS( 2 , 4, 'BS2' )


BS2 = Network.ActivateBS( 5 , 5, 'BS2' )
BS2 = Network.ActivateBS( 4 , 5, 'BS2' )
BS2 = Network.ActivateBS( 3 , 5, 'BS2' )
BS2 = Network.ActivateBS( 2 , 5, 'BS2' )

BS2 = Network.ActivateBS( 5 , 6, 'BS2' )
BS2 = Network.ActivateBS( 4 , 6, 'BS2' )
BS2 = Network.ActivateBS( 3 , 6, 'BS2' )

BS1.SetPower( P )
BS2.SetPower( P )
d1y = -1.0
d1x = 0.0

d2y = 1.0
d2x = Parameters('d1x')


U1 = UserCoopSIC( BS1, 'User1', [d1x,d1y] )
U2 = UserCoopSIC( BS2, 'User2', [d2x,d2y] )

U2.SetSICSlaves( [U1] )

Editor.AddNetworkModel('CoopSIC')
Network.ClearUsers()

U1 = UserOMA( BS1, 'U1', [d1x,d1y] )


VisualizeNetwork()
