import dearpygui.dearpygui as dpg
from User import User

class BaseStation:

	selected = False
	active = False

	users = []
	slavesBS = []

	index = (0,0)
	position = []
	polygonBS = None
	polygonColor = None

	P = 0 #dB

	def __init__(self, BS_points, position, TransmitPower, index ):
		self.slavesBS = []
		self.users = []
		self.P = TransmitPower
		self.index = index
		self.position = position
		self.polygonColor = [255,255,255,50]
		self.polygonBS = dpg.draw_polygon(points=BS_points, color=[255,255,255,50], thickness=2 )

	def setBSState( self, state ):
		if state:
			self.changeBSColor( [0,255,0,150], True )
		else:
			self.changeBSColor( [255,255,255,50], True )

		self.active = state 

	def addSlaveBS( self, BS ):
		self.slavesBS.append( BS )
		dpg.draw_polygon(parent="NetworkPlot",points=[ self.position , BS.position ], color=[0,255,255,150], thickness=1 )

	def selectBS( self , state ):
		self.selected = state
		if state:
			self.changeBSColor(  [0,255,255,255] , False )
		else:
			dpg.configure_item(item=self.polygonBS, color=self.polygonColor, thickness=2 )

	def changeBSColor( self , Color, saveColor ):
		if saveColor:
			self.polygonColor = Color 
		dpg.configure_item(item=self.polygonBS, color=Color, thickness=2)

	def addUser( self, position ):
		user = User( self, position )
		self.users.append( user )
		return user
