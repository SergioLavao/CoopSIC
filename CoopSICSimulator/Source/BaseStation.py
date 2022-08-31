import dearpygui.dearpygui as dpg
from User import User

#Base Station(BS): HexGridNetwork child, used for .

class BaseStation:

	#Antenna absolute position relative to HexGridNetwork, interferences are calculated based on this position.
	antenna_absolute_position = [0,0]
	active = False

	#Trisec Slave
	trisec_slave = False
	trisec_mainBS = None

	#Users in BS
	users = []

	#Used for SIC BSs Slaves 
	slavesBS = []

	#Index of HexGridNetwork (rows,cols)
	index = (0,0)

	#BS position relative to HexGridNetwork
	position = []

	#Visalization tools
	polygonBS = None
	polygonColor = None

	#BS Power[dB]
	P = 0

	def __init__( self, BS_points, position, TransmitPower, index ):
		self.slavesBS = []
		self.users = []
		self.trisec_slave = False
		self.trisec_mainBS = None
		self.P = TransmitPower
		self.index = index
		self.position = position
		self.antenna_absolute_position = position
		self.polygonColor = [255,255,255,50]
		self.polygonBS = dpg.draw_polygon(points=BS_points, color=[255,255,255,50], thickness=2 )

	#Set BS activation state
	def setBSState( self, state ):
		if state:
			self.changeBSColor( [0,255,0,150], True )
		else:
			self.changeBSColor( [255,255,255,50], True )

		self.active = state

	#If its called,BS will define the absolute position of trisec antenna.
	def setMainTrisecAntenna( self ):
		self.antenna_absolute_position = [self.position[0] + 1,self.position[1]]
		self.setTrisecAntenna( self )
		self.trisec_slave = False

	def setTrisecAntenna( self, Main_BS ):
		self.trisec_slave = True
		self.trisec_mainBS = Main_BS
		self.antenna_absolute_position = Main_BS.antenna_absolute_position
		dpg.draw_polygon(parent="NetworkPlot",points=[ Main_BS.antenna_absolute_position, self.position ], color=[255,0,255,150], thickness=1 )

	#Add SIC Slave to BS
	def addSlaveBS( self, BS ):
		self.slavesBS.append( BS )
		dpg.draw_polygon(parent="NetworkPlot",points=[ self.position , BS.position ], color=[0,255,255,150], thickness=1 )

	def changeBSColor( self , Color, saveColor ):
		if saveColor:
			self.polygonColor = Color 
		dpg.configure_item(item=self.polygonBS, color=Color, thickness=2)

	#Add user to BS
	def addUser( self, position ):
		user = User( self, position )
		self.users.append( user )
		return user