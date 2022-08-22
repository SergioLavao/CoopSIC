import dearpygui.dearpygui as dpg
import numpy as np

class User:

	relative_position = []
	absolute_position = []

	BS = None
	BS_SIC = None

	SINR = 0
	Capacity = 0

	UserCircle = None

	def __init__( self, BS, relative_position ):
		self.BS = BS
		self.relative_position = relative_position
		self.absolute_position = [ BS.position[0] + relative_position[0], BS.position[1] + relative_position[1] ]
		self.UserCircle = dpg.draw_circle( center = self.absolute_position, color=[255, 0, 0,255], fill=[255, 0, 0,255],radius=0.07, parent='NetworkPlot' )
		self.plotRay( BS.position, [255, 128, 0,50] )

	def getDistanceToBS( self ):
		distance = np.linalg.norm( np.array( self.absolute_position ) - np.array( self.BS.position ) )
		return distance

	def plotRay( self, vec2_to, color ):
		dpg.draw_polygon(parent="NetworkPlot",points=[ self.absolute_position , vec2_to ], color=color, thickness=1 )

	def changeColor( self , Color):
		dpg.configure_item(item=self.UserCircle, color=Color, thickness=2 )

	def setBSSIC( self, BS):
		self.BS_SIC = BS
		dpg.draw_polygon(parent="NetworkPlot",points=[ self.BS.position , BS.position ], color=[0,255,255,150], thickness=1 )

	def getCapacity( self ):
		self.SINR = self.BS.P * np.linalg.norm( self.relative_position )
		self.Capacity = np.log2( self.SINR + 1 )
		return self.Capacity