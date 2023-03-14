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

U1 = UserCoopSIC( BS1, 'User1', [d1x,d1y] )
U2 = UserCoopSIC( BS2, 'User2', [d2x,d2y] )
U3 = UserCoopSIC( BS3, 'User3', [d3x,d3y] )

Users = []

Users.append( BS1.users[0] )
Users.append( BS2.users[0] )
Users.append( BS3.users[0] )

Permutation = 0

maxCap = "CoopSICCapcity = max( [ "

#Orden 3
#for user_x in users:
#	for user_y in users:
#		if( user_x != user_y ):
#			for user_z in users:
#				if user_z != user_y and user_z!= user_x:
#					permutation += 1;
#					print( " % permutation ", user_x.alias, "->", user_y.alias, ",", user_z.alias)
#					user_x.setsicslaves( [user_y, user_z] )
#
#					alias = f'coopsic{user_x.alias}_{user_y.alias}{user_z.alias}'
#
#					editor.addnetworkmodel(alias)
#					
#					maxcap = maxcap + alias + " , "
#
#					for user in users:
#						user.clearparameters()

#Orden 2
for user_x in Users:
	for user_y in Users:
		if( user_x != user_y ):
			
			Permutation += 1;
			print( " % Permutation ", user_x.alias, "->", user_y.alias)
			user_x.SetSICSlaves( [user_y] )

			alias = f'CoopSIC{user_x.alias}_{user_y.alias}'

			Editor.AddNetworkModel(alias)
					
			maxCap = maxCap + alias + " , "

			for user in Users:
				user.ClearParameters()

maxCap = maxCap + " ]) "

print( maxCap )
VisualizeNetwork()