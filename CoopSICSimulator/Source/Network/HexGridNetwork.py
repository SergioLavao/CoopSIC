import sys
sys.path.append("../BaseStation")

from BaseStation import BaseStation
from NetworkViewport import NetworkViewport

#HexGridNetwork (Singleton!): Defines the network based on a size[nxn] with hexagonal topology
class HexGridNetwork( NetworkViewport ):

	BSs = None

	def __init__( self , network_size, hexagonal_radius=1 ):

		super().__init__( network_size, hexagonal_radius )

		self.BSs = []

		for i in range( network_size[1] ):
			for j in range( network_size[0] ):
				self.BSs.append( BaseStation( (j,i), hexagonal_radius ) )

	def ActivateBS( self, row, column ):
		for BS in self.BSs:
			if BS.index == ( row , column ):
				BS.Activate()
				return BS

	def ClearUsers( self ):
		for BS in self.BSs:
			BS.users.clear()