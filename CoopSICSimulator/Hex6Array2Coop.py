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

BS1 = HexGrid.activateBS( 0, 1 )#Get BS via row, column
BS2 = HexGrid.activateBS( 1, 2 )#Get BS via row, column

BS3 = HexGrid.activateBS( 1, 1 )#Get BS via row, column
BS4 = HexGrid.activateBS( 2, 2 )#Get BS via row, column

BS5 = HexGrid.activateBS( 2, 1 )#Get BS via row, column
BS6 = HexGrid.activateBS( 3, 2 )#Get BS via row, column

BS1.addSlaveBS( BS2 )
U1 = BS1.addUser([x_edge,y_edge])
U1_Slave = BS2.addUser([-x_edge,-y_edge])

BS3.addSlaveBS( BS4 )
U2 = BS3.addUser([x_edge,y_edge])
U2_Slave = BS4.addUser([-x_edge,-y_edge])

BS5.addSlaveBS( BS6 )
U3 = BS5.addUser([x_edge,y_edge])
U3_Slave = BS6.addUser([-x_edge,-y_edge])


HexGrid.getUser_f_rho( U3, alpha , True )
HexGrid.getNetworkCapacity( alpha )

dpg.start_dearpygui()
dpg.destroy_context()