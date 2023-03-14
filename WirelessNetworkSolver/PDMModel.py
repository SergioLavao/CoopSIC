import sys
sys.path.append("./Source")

from WirelessNetworkSolver import *

P = Parameter('P')

N_0, W, rho, alpha = Parameters('N_0 W rho alpha')

edge_distance = 1
radius = SetRadiusFromEdge( edge_distance ) 
  
Network = HexGridNetwork( [3,3], radius )
Network.SetNetworkParameters( W, rho, N_0, alpha, P )
Editor = NetworkEditor( Network )

Users = []

BS1 = Network.ActivateBS( 1 , 1, 'BS1' )
BS2 = Network.ActivateBS( 0 , 1, 'BS2' )
BS3 = Network.ActivateBS( 1 , 0, 'BS3' )

BS1.SetPower( P )
BS2.SetPower( P )
BS3.SetPower( P )

d1y = Parameter('d1y')
d1x = Parameter('d1x')

d2y = Parameter('d2y')
d2x = Parameter('d2x')

d3y = Parameter('d3y')
d3x = Parameter('d3x')

U1 = UserIaN( BS1, '1', [d1x,d1y] )
U2 = UserIaN( BS2, '2', [d2x,d2y] )
U3 = UserIaN( BS3, '3', [d3x,d3y] )

Users = [ U1, U2, U3 ]

for user_x in Users:
	for user_y in Users:
		print( "P_" + user_x.alias + user_y.alias + " = " + MatlabExpression( f'{ sym.N( P * user_x.ChannelFadingGain( user_y.BS , alpha ), 3 )}' ) + ';' )