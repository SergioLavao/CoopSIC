import sys
sys.path.append("../Source")

from WirelessNetworkSolver import *

P = Parameter('P')

N_0, W, rho, alpha = Parameters('N_0 W rho alpha')

edge_distance = 1
radius = SetRadiusFromEdge( edge_distance ) 
  
Network = HexGridNetwork( [3,3], radius )
Network.SetNetworkParameters( W, rho, N_0, alpha, P )
Editor = NetworkEditor( Network )

BS1 = Network.ActivateBS( 1 , 1, 'BS1' )
BS2 = Network.ActivateBS( 0 , 1, 'BS2' )
BS3 = Network.ActivateBS( 1 , 0, 'BS3' )

BS4 = Network.ActivateBS( 0 , 0, 'BS4' )
BS5 = Network.ActivateBS( 2 , 0, 'BS5' )
BS6 = Network.ActivateBS( 1 , 2, 'BS6' )

BS4.ChangeColor( [50,150,200] )
BS5.ChangeColor( [50,150,200] )
BS6.ChangeColor( [50,150,200] )

BS1.SetPower( P )
BS2.SetPower( P )
BS3.SetPower( P )
BS4.SetPower( P )
BS5.SetPower( P )
BS6.SetPower( P )


d1y = Parameter('d1y')
d1x = Parameter('d1x')

d2y = Parameter('d2y')
d2x = Parameter('d2x')

d3y = Parameter('d3y')
d3x = Parameter('d3x')

U1 = UserIaN( BS1, 'User1', [d1x,d1y] )
U2 = UserIaN( BS2, 'User2', [d2x,d2y] )
U3 = UserIaN( BS3, 'User3', [d3x,d3y] )

Editor.AddNetworkModel("IaN")
		
VisualizeNetwork()