import math 
import numpy as np
import dearpygui.dearpygui as dpg

from BaseStation import BaseStation

#HexGrid (Singleton!): Defines the network based on a size[nxn] 

class HexGrid:

	d = 0 #Distance to cell corner
	N = 0 #Active BSs
	BSs = []

	def __init__( self, networkSize, hex_radius ):
		self.d = hex_radius

		dpg.create_context()

		dpg.create_viewport(title="Hex Grid Network", x_pos=0, y_pos=0, width=600, height=600)
		dpg.set_viewport_max_height(600)
		dpg.set_viewport_max_width(600)

		with dpg.window(tag="Primary Window") as main_window:
			with dpg.plot( no_menus=False, no_title=True, no_box_select=False, no_mouse_pos=False, width=500,
				height=500, equal_aspects=True, tag="NetworkPlot" ) as SIMWorld:

				axis_x = dpg.add_plot_axis(axis=0,label="X Axis[km]", lock_min=True,lock_max=True)
				dpg.set_axis_limits(axis=axis_x, ymin=0, ymax=networkSize[1]*hex_radius*2)

				axis_y = dpg.add_plot_axis(axis=1,label="Y Axis[km]", lock_min=True,lock_max=True)
				dpg.set_axis_limits(axis=axis_y, ymin=0, ymax=networkSize[0]*hex_radius*2)

				x_ref = hex_radius*math.cos( np.pi / 3 )	
				y_ref = hex_radius*math.sin( np.pi / 3 )	

				for i in range( networkSize[1] ):
					x_pos =	2*hex_radius + i*hex_radius + i*x_ref

					for j in range( networkSize[0] ):
						y_pos = j*2*y_ref + y_ref + hex_radius/4 
						
						if (i % 2) != 0:
							y_pos = y_pos + y_ref 

						BS_pos = [ x_pos , y_pos ]
						BS_points = [ [ hex_radius + BS_pos[0], BS_pos[1] ],
							[ x_ref + BS_pos[0], y_ref + BS_pos[1] ],
							[ -x_ref + BS_pos[0], y_ref + BS_pos[1] ],
							[ -hex_radius + BS_pos[0], BS_pos[1] ],
							[ -x_ref + BS_pos[0], -y_ref + BS_pos[1] ],
							[ x_ref + BS_pos[0], -y_ref + BS_pos[1] ],
							[ hex_radius + BS_pos[0], BS_pos[1] ] ]

						BS = BaseStation( BS_points, BS_pos, 1 ,(j,i) )
						self.BSs.append(BS)

		dpg.setup_dearpygui()
		dpg.show_viewport()
		dpg.set_primary_window(window=main_window, value=True)

	def activateBS( self, row, column ):
		self.N = self.N + 1 
		for BS in self.BSs:
			if BS.index == ( row , column ):
				BS.setBSState( True )
				return BS

	def getUser_f_rho( self , user, alpha, visualizeInterference ):
		
		f_rho = 0
		distance_BS_User = user.getDistanceToBS()

		for BS in self.BSs:
			if BS.active:
				if BS != user.BS and BS not in user.BS.slavesBS and not BS.trisec_slave and BS != user.BS.trisec_mainBS:
					f_rho = f_rho + np.power( np.linalg.norm( np.array( user.absolute_position ) - np.array( BS.antenna_absolute_position ) ) , -alpha )
					if visualizeInterference:
						user.plotRay( BS.antenna_absolute_position, [255,0,0,100] )

		f_rho = f_rho * np.power( self.d , alpha ) 
		return f_rho

	def getUserCapacity( self, index, user, alpha, visualize ):
		return f"C_U{index} = rho * log2( 1 + ( (SNR * { round( np.power( user.getDistanceToBS() / self.d  , -alpha), 4) } )./ ( rho + { round( self.getUser_f_rho( user, alpha , visualize ), 4 ) } .* SNR ) ) );"

	def getNetworkCapacity( self, alpha ):
		index = 0

		Network_Capacity = 'NetworkCapacity = '

		for BS in self.BSs:
			for user in BS.users: 
				index = index + 1
				print( self.getUserCapacity( index, user, alpha, True ) )
				Network_Capacity = Network_Capacity + f' C_U{index} +' 

		print( Network_Capacity, ';' )
		print( f'NetworkCapacityNormalized = NetworkCapacity / {self.N}; %[NetCap/Cells] ' )

	def activateTrisec( self, row , col ):
		
		fixed_row = row
		fixed_col = col

		if row % 2 != 0:
			fixed_col = col + 1
		else:
			fixed_col = col + 1

		if col % 2 != 0:
			fixed_row = row + 1
		else:
			fixed_row = row - 1

		BS1 = self.activateBS( row, col )#Get BS via row, column
		BS2 = self.activateBS( row, fixed_col )#Get BS via row, column
		BS3 = self.activateBS( fixed_row, fixed_col )#Get BS via row, column

		BS1.setMainTrisecAntenna()
		BS2.setTrisecAntenna( BS1 )
		BS3.setTrisecAntenna( BS1 )

		return [BS1, BS2, BS3]