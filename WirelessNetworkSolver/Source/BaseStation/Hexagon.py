import math 
import numpy as np
import dearpygui.dearpygui as dpg

#Base Station(BS): HexGridNetwork child, used for topology and visual purposes in the HexGrid.
class Hexagon:

	index = (0,0)
	position = []

	#Visalization tools
	polygon = None

	hexagonPoints = []

	def __init__( self, index, radius ):
		self.index = index
		polygon_points = self.CreateGeometry( index[0],index[1], radius )
		self.polygon = dpg.draw_polygon( points=polygon_points, color=[255,255,255,50] , thickness=2,parent='NetworkPlot' )

	def CreateGeometry( self, j , i , radius ) -> []:
		x_ref = radius*math.cos( np.pi / 3 )	
		y_ref = radius*math.sin( np.pi / 3 )	

		x_pos =	2*radius + i*radius + i*x_ref
		y_pos = j*2*y_ref + y_ref + radius/4
		
		if (i % 2) != 0:
			y_pos = y_pos + y_ref 

		position = [ x_pos , y_pos ]
		self.position = position

		points = [ [ radius + position[0], position[1] ],
			[ x_ref + position[0], y_ref + position[1] ],
			[ -x_ref + position[0], y_ref + position[1] ],
			[ -radius + position[0], position[1] ],
			[ -x_ref + position[0], -y_ref + position[1] ],
			[ x_ref + position[0], -y_ref + position[1] ],
			[ radius + position[0], position[1] ] ]

		self.hexagonPoints = points
		return points

	def plotRay( self, f , t , color):
		dpg.draw_polygon(parent="NetworkPlot",points=[ f , t ], color=color, thickness=1 )

	def ChangeColor( self , Color ):
		dpg.configure_item( item=self.polygon , color=Color , thickness=2 )

	def GetHexagonPoints( self ):
		return self.hexagonPoints