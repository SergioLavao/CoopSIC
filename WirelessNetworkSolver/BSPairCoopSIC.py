import sys
sys.path.append("./Source")

from WirelessNetworkSolver import *

W = 1
rho = 1
N_0 = 1
alpha = Parameter("alpha")
P = Parameter("P")

distance_to_edge = 1.0
Network = HexGridNetwork( [2,2], SetRadiusFromEdge( distance_to_edge ) )
Network.SetNetworkParameters( W, rho, N_0, alpha, P )

Editor = NetworkEditor( Network )

BS1 = Network.ActivateBS( 1 , 0, 'BS1' )
BS2 = Network.ActivateBS( 0 , 0, 'BS2' )

BS1.SetPower( P )
BS2.SetPower( P )

d1y = Parameter("d1y");
d1x = Parameter("d1x");

d2y = Parameter("d2y");
d2x = Parameter("d2x");

U1 = UserCoopSIC( BS1, 'User1', [d1x,d1y] )
U2 = UserCoopSIC( BS2, 'User2', [d2x,d2y] )

U1.SetSICSlaves([ U2 ])

Editor.AddNetworkModel('CoopSIC')

d1y = Parameter("d1y");
d1x = Parameter("d1x");

d2y = Parameter("d2y");
d2x = Parameter("d2x");

U1 = UserCoopSIC( BS1, 'User1', [d1x,d1y] )
U2 = UserCoopSIC( BS2, 'User2', [d2x,d2y] )

U2.SetSICSlaves([ U1 ])

Editor.AddNetworkModel('CoopSICU2Master')

U1 = UserOMA( BS1, 'User1', [d1x,d1y] )
U1.SetOMAParameters( Parameter("alpha_W") ,1 )
U2 = UserOMA( BS2, 'User2', [d2x,d2y]  )
U2.SetOMAParameters( 1 - Parameter("alpha_W"),1 )

Editor.AddNetworkModel('OMA')

U1 = UserIaN( BS1, 'User1', [d1x,d1y] )
U2 = UserIaN( BS2, 'User2', [d2x,d2y]  )

Editor.AddNetworkModel('IaN')

VisualizeNetwork()