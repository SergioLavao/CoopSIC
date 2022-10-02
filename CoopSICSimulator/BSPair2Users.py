import sys
sys.path.append("./Source")

from WirelessNetworkSolver import *

#Linear Network

distanceToEdge = 1.0 #meters
distanceToCorner = SetRadiusFromEdge( distanceToEdge )

Network = HexGridNetwork( [4,4], distanceToCorner )
#Network.SetNetworkParameters( Parameter('W'), Parameter('rho'), Parameter('N_0'), Parameter('alpha'),Parameter('P') )
Network.SetNetworkParameters( 1, 1, 1, 3,Parameter('P') )

U1Position = [0.577,1.0]#[Parameter('d1_x'),Parameter('d1_y')]
U2Position = [0.577,-1.0]
U3Position = [-float(distanceToCorner),0.0]

U12Position = [0.577,1.0]#[Parameter('d1_x'),Parameter('d1_y')]
U22Position = [0.577,-1.0]
U32Position = [-float(distanceToCorner),0.0]

U13Position = [0.577,1.0]#[Parameter('d1_x'),Parameter('d1_y')]
U23Position = [0.577,-1.0]
U33Position = [-float(distanceToCorner),0.0]


Editor = NetworkEditor( Network )

BS1 = Network.ActivateBS( 1 , 1, 'BS1' )
BS2 = Network.ActivateBS( 2 , 1, 'BS2' )
BS3 = Network.ActivateBS( 2 , 2, 'BS3' )

#Ring of interference
def ActivateRing():
	Network.ActivateBS( 3 , 2, 'BS4' )
	Network.ActivateBS( 3 , 1, 'BS5' )
	Network.ActivateBS( 3 , 0, 'BS6' )
	Network.ActivateBS( 2 , 0, 'BS7' )
	Network.ActivateBS( 1 , 2, 'BS8' )
	Network.ActivateBS( 1 , 0, 'BS9' )
	Network.ActivateBS( 0 , 1, 'BS10' )

#ActivateRing()

U1 = UserIaN( BS1, 'User1', U1Position )
U2 = UserIaN( BS2, 'User2', U2Position )
U3 = UserIaN( BS3, 'User3', U3Position )
U12 = UserIaN( BS1, 'User12', U12Position )
U22 = UserIaN( BS2, 'User22', U22Position )
U32 = UserIaN( BS3, 'User32', U32Position )
U13 = UserIaN( BS1, 'User13', U13Position )
U23 = UserIaN( BS2, 'User23', U23Position )
U33 = UserIaN( BS3, 'User33', U33Position )


Editor.AddNetworkModel('IaN_Network')

alpha = 1/9

U1 = UserOMA( BS1, 'User1', U1Position )
U2 = UserOMA( BS2, 'User2', U2Position )
U3 = UserOMA( BS3, 'User3', U3Position )
U12 = UserOMA( BS1, 'User12', U12Position )
U22 = UserOMA( BS2, 'User22', U22Position )
U32 = UserOMA( BS3, 'User32', U32Position )
U13 = UserOMA( BS1, 'User13', U13Position )
U23 = UserOMA( BS2, 'User23', U23Position )
U33 = UserOMA( BS3, 'User33', U33Position )

U1.SetAlpha( alpha )
U2.SetAlpha( alpha )
U3.SetAlpha( alpha )
U12.SetAlpha( alpha )
U22.SetAlpha( alpha )
U32.SetAlpha( alpha )
U13.SetAlpha( alpha )
U23.SetAlpha( alpha )
U33.SetAlpha( alpha )

Editor.AddNetworkModel('OMA_Network')

U1 = UserCoopSIC( BS1, 'User1', U1Position )
U2 = UserCoopSIC( BS2, 'User2', U2Position )
U3 = UserCoopSIC( BS3, 'User3', U3Position )
U12 = UserCoopSIC( BS1, 'User12', U12Position )
U22 = UserCoopSIC( BS2, 'User22', U22Position )
U32 = UserCoopSIC( BS3, 'User32', U32Position )
U13 = UserCoopSIC( BS1, 'User13', U13Position )
U23 = UserCoopSIC( BS2, 'User23', U23Position )
U33 = UserCoopSIC( BS3, 'User33', U33Position )
#U1.SetSICSlaves( [ U2,U3,U22,U32,U23,U33 ] )
U12.SetSICSlaves( [ U22,U32 ] )
U13.SetSICSlaves( [ U23,U33 ] )

Editor.AddNetworkModel('Coop_SIC_Network')

U1 = UserPDM( BS1, 'User1', U1Position )
U2 = UserPDM( BS2, 'User2', U2Position )
U3 = UserPDM( BS3, 'User3', U3Position )
U12 = UserPDM( BS1, 'User12', U12Position )
U22 = UserPDM( BS2, 'User22', U22Position )
U32 = UserPDM( BS3, 'User32', U32Position )
U13 = UserPDM( BS1, 'User13', U13Position )
U23 = UserPDM( BS2, 'User23', U23Position )
U33 = UserPDM( BS3, 'User33', U33Position )
U1.SetSICSlaves( [ U12,U13] )
U2.SetSICSlaves( [ U22,U23] )
U3.SetSICSlaves( [ U32,U33] )


Editor.AddNetworkModel('PDM_Network')

VisualizeNetwork()