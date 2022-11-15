import sys
sys.path.append("../BaseStation")

from BaseStation import BaseStation
from NetworkViewport import NetworkViewport

#HexGridNetwork (Singleton!): Defines the network based on a size[nxn] with hexagonal topology
class HexGridNetwork( NetworkViewport ):

	alias = ''
	BSs = None

	W = 1
	rho = 1
	N_0 = 1
	alpha = 1
	BSPower = 1

	def __init__( self , network_size, hexagonal_radius=1 ):

		super().__init__( network_size, hexagonal_radius )

		self.BSs = []

		for i in range( network_size[1] ):
			for j in range( network_size[0] ):
				self.BSs.append( BaseStation( (j,i), hexagonal_radius ) )

	def SetNetworkParameters( self, W, rho, N_0, alpha, BSPower ):
		self.W = W
		self.rho = rho
		self.N_0 = N_0
		self.alpha = alpha
		self.BSPower = BSPower

	def ActivateBS( self, row, column, alias='BS' ):
		for BS in self.BSs:
			if BS.index == ( row , column ):
				BS.Activate()
				BS.SetPower( self.BSPower )
				BS.alias = alias
				return BS

	def ClearUsers( self ):
		for BS in self.BSs:
			BS.users.clear()