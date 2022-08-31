import sys
import numpy as np
import dearpygui.dearpygui as dpg
sys.path.append("./Source")

from HexGridGen import HexGrid

d = 1 #Distance to edge 
x_corner = d*np.cos(np.pi/3)
y_corner = d*np.sin(np.pi/3)

HexGrid = HexGrid( [6,6] , d )

alpha = 3

#SIC Group 1
HexGrid.activateTrisec( 0,1 )
HexGrid.activateTrisec( 0,3 )

#Right
HexGrid.activateTrisec( 2,4 )

#Upper
HexGrid.activateTrisec( 3,3 )
HexGrid.activateTrisec( 3,1 )

#Left
HexGrid.activateTrisec( 2,0 )

#Center 
[BS1,BS2,BS3] = HexGrid.activateTrisec( 2,2 )

BS1.addUser([0,0])

dpg.start_dearpygui()
dpg.destroy_context()