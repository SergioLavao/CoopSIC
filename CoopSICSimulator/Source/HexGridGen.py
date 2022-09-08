import math 
import numpy as np
import dearpygui.dearpygui as dpg

from BaseStation import BaseStation

import sympy as sym

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
				height=500, equal_aspects=True, tag="NetworkPlot" ) as NetworkCanvas:

				axis_x = dpg.add_plot_axis(axis=0,label="X Axis[km]", lock_min=True,lock_max=True)
				dpg.set_axis_limits(axis=axis_x, ymin=0, ymax=networkSize[1]*hex_radius*2)

				axis_y = dpg.add_plot_axis(axis=1,label="Y Axis[km]", lock_min=True,lock_max=True)
				dpg.set_axis_limits(axis=axis_y, ymin=0, ymax=networkSize[0]*hex_radius*2)

		dpg.setup_dearpygui()
		dpg.show_viewport()
		dpg.set_primary_window(window=main_window, value=True)

		for i in range( networkSize[1] ):
			for j in range( networkSize[0] ):
				self.BSs.append( BaseStation( (j,i), hex_radius ) )

	def ActivateBS( self, row, column ):
		for BS in self.BSs:
			if BS.index == ( row , column ):
				BS.Activate()
				return BS

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