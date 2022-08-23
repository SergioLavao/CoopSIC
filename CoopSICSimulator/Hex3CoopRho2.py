import sys
import numpy as np
import dearpygui.dearpygui as dpg
sys.path.append("./Source")

from HexGridGen import HexGrid

d = 1 #Distance to edge 
x_corner = d*np.cos(np.pi/3)
y_corner = d*np.sin(np.pi/3)

HexGrid = HexGrid( [5,5] , d )

alpha = 3

#SIC Group 1
BS1 = HexGrid.activateBS( 4, 4 )#Get BS via row, column
BS2 = HexGrid.activateBS( 4, 3 )#Get BS via row, column
BS3 = HexGrid.activateBS( 3, 3 )#Get BS via row, column

#BS1.addSlaveBS( BS2 )
#BS1.addSlaveBS( BS3 )
U1 = BS1.addUser([-d,0])
U1_Slave1 = BS2.addUser([x_corner,-y_corner]),
U1_Slave2 = BS3.addUser([x_corner,y_corner]),


#SIC Group 2
BS4 = HexGrid.activateBS( 2, 2 )#Get BS via row, column
BS5 = HexGrid.activateBS( 1, 3 )#Get BS via row, column
BS6 = HexGrid.activateBS( 1, 2 )#Get BS via row, column

#BS4.addSlaveBS( BS5 )
#BS4.addSlaveBS( BS6 )
U2 = BS4.addUser([x_corner,-y_corner])
U2_Slave1 = BS5.addUser([-d,0]),
U2_Slave2 = BS6.addUser([x_corner,y_corner]),

#SIC Group 3
BS7 = HexGrid.activateBS( 3, 0 )#Get BS via row, column
BS8 = HexGrid.activateBS( 2, 1 )#Get BS via row, column
BS9 = HexGrid.activateBS( 2, 0 )#Get BS via row, column

#BS7.addSlaveBS( BS8 )
#BS7.addSlaveBS( BS9 )
U3 = BS7.addUser([x_corner,-y_corner])
U3_Slave1 = BS8.addUser([-d,0]),
U3_Slave2 = BS9.addUser([x_corner,y_corner]),

HexGrid.getNetworkCapacity( alpha )

dpg.start_dearpygui()
dpg.destroy_context()