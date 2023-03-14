import sys
sys.path.append("../Source")

from WirelessNetworkSolver import *

P = Parameter('P')
beta = Parameter('beta')

N_0, W, rho, alpha = Parameters('N_0 W rho alpha')

edge_distance = 1
radius = SetRadiusFromEdge( edge_distance ) 
  
Network = HexGridNetwork( [3,3], radius )
Editor = NetworkEditor( Network )

BS1 = Network.ActivateBS( 1 , 1, 'BS1' )
BS2 = Network.ActivateBS( 0 , 1, 'BS2' )
BS3 = Network.ActivateBS( 1 , 0, 'BS3' )
BS4 = Network.ActivateBS( 1 , 2, 'BS4' )

BS1.SetPower( P )
BS2.SetPower( P )
BS3.SetPower( P )
BS4.SetPower( P )

d1y = -1.0
d1x = 0.0

d2y = 1.0
d2x = 0.0

U1 = UserCoopSIC( BS1, 'User1', [d1x,d1y] )
U2 = UserCoopSIC( BS2, 'User2', [d2x,d2y] )

U2.SetSICSlaves( [U1] )

Editor.AddNetworkModel('CoopSIC')
Network.ClearUsers()

U1 = UserOMA( BS1, f'User1', [d1x,d1y] )
U1.SetOMAParameters( 1/4, 1 )
U2 = UserOMA( BS2, f'User2', [d2x,d2y] )
U2.SetOMAParameters( 1/4, 1 )

Editor.AddNetworkModel('OMA')
Network.ClearUsers()

VisualizeNetwork()
