import sys
import numpy as np
import dearpygui.dearpygui as dpg
sys.path.append("./Source")

from HexGridGen import HexGrid

d = 1 #Distance to corner

y_bound = d*np.cos(np.pi/6)
x_edge = y_bound*np.cos(np.pi/6)
y_edge = y_bound*np.sin(np.pi/6)

HexGrid = HexGrid( [5,5] , d )

alpha = 3
rho = 1

#Group 1
BS1 = HexGrid.activateBS( 0, 0 )#Get BS via row, column
BS2 = HexGrid.activateBS( 0, 1 )#Get BS via row, column
#
#BS1.addSlaveBS( BS2 )
U1 = BS1.addUser([x_edge,y_edge])
U1_Slave = BS2.addUser([-x_edge,-y_edge])

#Group 2
BS3 = HexGrid.activateBS( 2, 0 )#Get BS via row, column
BS4 = HexGrid.activateBS( 2, 1 )#Get BS via row, column
#
#BS3.addSlaveBS( BS4 )
U2 = BS3.addUser([x_edge,y_edge])
U2_Slave = BS4.addUser([-x_edge,-y_edge])

#Group 3
BS5 = HexGrid.activateBS( 4, 0 )#Get BS via row, column
BS6 = HexGrid.activateBS( 4, 1 )#Get BS via row, column
#
#BS5.addSlaveBS( BS6 )
U3 = BS5.addUser([x_edge,y_edge])
U3_Slave = BS6.addUser([-x_edge,-y_edge])

#Group 4
BS7 = HexGrid.activateBS( 4, 2 )#Get BS via row, column
BS8 = HexGrid.activateBS( 4, 3 )#Get BS via row, column
#
#BS7.addSlaveBS( BS8 )
U3 = BS7.addUser([x_edge,y_edge])
U3_Slave = BS8.addUser([-x_edge,-y_edge])

#Group 5
BS9 = HexGrid.activateBS( 2, 2 )#Get BS via row, column
BS10 = HexGrid.activateBS( 2, 3 )#Get BS via row, column
#
#BS9.addSlaveBS( BS10 )
U4 = BS9.addUser([x_edge,y_edge])
U4_Slave = BS10.addUser([-x_edge,-y_edge])

#Group 6
BS11 = HexGrid.activateBS( 0, 2 )#Get BS via row, column
BS12 = HexGrid.activateBS( 0, 3 )#Get BS via row, column

##S11.addSlaveBS( BS12 )
U5 = BS11.addUser([x_edge,y_edge])
U5_Slave = BS12.addUser([-x_edge,-y_edge])

HexGrid.getNetworkCapacity( alpha )

dpg.start_dearpygui()
dpg.destroy_context()