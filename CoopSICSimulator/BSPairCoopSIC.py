import sys
sys.path.append("./Source")

from WirelessNetworkSolver import *

#Linear Network
W = Parameter('W')
rho = Parameter('rho')
N_0 = Parameter('N_0')
alpha = Parameter('alpha')
P = Parameter('P')


distance_to_edge = 1.0
Network = HexGridNetwork( [2,2], SetRadiusFromEdge( distance_to_edge ) )
Network.SetNetworkParameters( Parameter('W'), Parameter('rho'), Parameter('N_0'), Parameter('alpha'), Parameter('P') )

Editor = NetworkEditor( Network )

BS1 = Network.ActivateBS( 1 , 0, 'BS1' )
BS2 = Network.ActivateBS( 0 , 0, 'BS2' )

BS1.SetPower( P )
BS2.SetPower( P )

print( " BS1Pos =", np.array( BS1.antenna_absolute_position ) )
print( " BS2Pos =", np.array( BS2.antenna_absolute_position ) )
BS1.GetMatlabPlot()
BS2.GetMatlabPlot()

d2x = Parameter('d1x_rel');
d2y = Parameter('d1y_rel');

U1 = UserCoopSIC( BS1, 'User2', [d2x,d2y] )
U2 = UserCoopSIC( BS2, 'User1', [0.0,1.0] )
print( " U2Pos =", np.array(U2.absolute_position) )

U1.SetSICSlaves([ U2 ])

Editor.AddNetworkModel('CoopSIC')

U1 = UserOMA( BS1, 'User2', [d2x,d2y] )
U1.SetOMAParameters( 1/2,1 )
U2 = UserOMA( BS2, 'User1', [0.0,1.0]  )
U2.SetOMAParameters( 1/2,1 )

Editor.AddNetworkModel('OMA')

U1 = UserIaN( BS1, 'User2', [d2x,d2y] )
U2 = UserIaN( BS2, 'User1', [0.0,1.0]  )

Editor.AddNetworkModel('IaN')

VisualizeNetwork()