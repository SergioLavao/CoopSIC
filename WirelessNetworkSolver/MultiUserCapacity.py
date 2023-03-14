import sys
sys.path.append("./Source")

from WirelessNetworkSolver import *

#OMA and CoopSIC Performance over N Users

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

NUsers = 10

UsersCoopSIC = []
UserCoopSICCapacities = []

UsersOMA = []
UsersOMACapacities = []

Capacity = 0
for i in range(1,NUsers + 1):
	if i % 2 == 0:
		UsersCoopSIC.append( UserCoopSIC( BS1, f'User{i}', [d1x,d1y] ) )
	else:
		UsersCoopSIC.append( UserCoopSIC( BS2, f'User{i}', [d2x,d2y] ) )

for i in range(0,NUsers - 1):
	if i % 2 == 0:
		UsersCoopSIC[i].SetSICSlaves([ UsersCoopSIC[i + 1] ])

for user in UsersCoopSIC:
	Capacity = Capacity + user.GetNumericCapacity( Network, N_0, W, rho, alpha ) 

UserCoopSICCapacities.append( Capacity )
Network.ClearUsers()

Capacity = 0
for i in range(1,NUsers + 1):
	if i % 2 == 0:
		U = UserOMA( BS1, f'User{i}', [d1x,d1y] )
		U.SetOMAParameters( 1/NUsers,1 )
		UsersOMA.append( U )
	else:
		U = UserOMA( BS2, f'User{i}', [d2x,d2y] )
		U.SetOMAParameters( 1/NUsers,1 )
		UsersOMA.append( U )

for user in UsersOMA:
	Capacity = Capacity + user.GetNumericCapacity( Network, N_0, W, rho, alpha ) 

UsersOMACapacities.append( Capacity )
Editor.AddNetworkModel('OMA')

Network.ClearUsers()

print( UserCoopSICCapacities )
print( UsersOMACapacities )

VisualizeNetwork()