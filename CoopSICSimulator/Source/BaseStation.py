import dearpygui.dearpygui as dpg
import numpy as np
from User import User

import sympy as sym

from Hexagon import Hexagon

class BaseStation( Hexagon ):

	#BS Power[dB]
	Power = 0

	#Antenna absolute position relative to HexGridNetwork, interferences are calculated based on this position.
	users = []
	active = False
	antenna_absolute_position = [0,0]


	def __init__( self, index, radius ):
		super().__init__( index, radius )

		self.Power = 60
		self.users = []
		self.antenna_absolute_position = self.position

	def SetPower( self, Power ):
		self.Power = Power

	#Set BS activation state
	def Activate( self ):
		self.ChangeColor( [0,255,0,150] )
		self.active = True

	#Add user to BS
	def AddUser( self, alias="User", position=[0.0,0.0] ):
		user = User( self, alias, position )
		self.users.append( user )
		return user