import dearpygui.dearpygui as dpg

class NetworkViewport:

	def __init__( self, networkSize, hex_radius=1 ):

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
