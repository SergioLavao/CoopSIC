import dearpygui.dearpygui as dpg
import sympy as sym
import numpy as np

class UserBase:

	alias = ''

	relative_position = []
	absolute_position = []

	BS = None

	sinr = 0

	def __init__( self, BS, alias, relative_position ):

		BS.AddUser( self )

		self.BS = BS
		self.alias = alias
		self.relative_position = relative_position
		self.absolute_position = [ BS.position[0] + relative_position[0], BS.position[1] + relative_position[1] ]
		
		if type(relative_position[0]) is float and type(relative_position[1]) is float:
			dpg.draw_circle( center = self.absolute_position, color=[255, 0, 0,255], fill=[255, 0, 0,255],radius=0.07, parent='NetworkPlot' )
			self.plotRay( BS.antenna_absolute_position, [255, 128, 0,50] )
		else:
			dpg.draw_circle( center = BS.antenna_absolute_position, color=[255, 0, 255,255], fill=[255, 0, 255,255],radius=0.07, parent='NetworkPlot' )			

	def EuclideanDistance( self, pos1, pos2):
		'''Returns the euclidean distance in the R2 space (positions can be symbolic)'''
		euclidean_distance = sym.sqrt( sym.Pow( pos1[0] - pos2[0], 2 ) + sym.Pow( pos1[1] - pos2[1], 2 ) )
		return euclidean_distance

	def ChannelFadingGain( self , BS, alpha ):
		'''Simple fading gain |h|^2 = d^-alpha'''
		return  np.power( self.DistanceTo( BS.antenna_absolute_position ) , -alpha )

	def DistanceTo( self, position ):
		'''Returns the euclidean distance from the user absolute position to a desired BS antenna.'''
		return ( self.EuclideanDistance( self.absolute_position , position  ) )

	def plotRay( self, vec2_to, color ):
		dpg.draw_polygon(parent="NetworkPlot",points=[ self.absolute_position , vec2_to ], color=color, thickness=1 )