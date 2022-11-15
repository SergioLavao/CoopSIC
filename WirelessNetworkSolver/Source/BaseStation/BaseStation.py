import dearpygui.dearpygui as dpg
import numpy as np

from UserIaN import UserIaN
from Hexagon import Hexagon

class BaseStation( Hexagon ):

	#BS Power[dB]
	Power = 0

	alias = 'BS'

	#Antenna absolute position relative to HexGridNetwork, interferences are calculated based on this position.
	users = []
	active = False
	antenna_absolute_position = [0,0]

	def __init__( self, index, radius ):
		super().__init__( index, radius )

		self.radius = radius
		self.Power = 60
		self.users = []
		self.antenna_absolute_position = self.position

	def SetAntennaRelativePosition( self, relativePosition ):
		self.antenna_absolute_position = [self.position[0] + relativePosition[0] , self.position[1] + relativePosition[1]]
		self.plotRay( self.position, self.antenna_absolute_position, [255,0,255,255] )

	def SetAntennaAbsolutePosition( self, absolutePosition ):
		self.antenna_absolute_position = absolutePosition
		self.plotRay( self.position, self.antenna_absolute_position, [255,0,255,255] )

	def SetPower( self, Power ):
		self.Power = Power

	def SetPowerDB( self, Power ):
		self.Power = np.power( 10 , Power / 10) 

	#Set BS activation state
	def Activate( self ):
		self.ChangeColor( [0,255,0,150] )
		self.active = True

	def Deactivate( self ):
		self.ChangeColor( [255,255,255,50] )
		self.active = True

	#Add user to BS
	def AddUser( self, user ):
		self.users.append( user )
		return user

	def GetMatlabPlot( self ):
		print( f'{self.alias}polygonX =', np.array(self.GetHexagonPoints())[:,0],";" )
		print( f'{self.alias}polygony =', np.array(self.GetHexagonPoints())[:,1],";" )
