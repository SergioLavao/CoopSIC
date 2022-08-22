import sys
import numpy as np
import dearpygui.dearpygui as dpg
sys.path.append("./Source")

from HexGridGen import HexGrid

d = 1 #Distance to edge 

HexGrid = HexGrid( [5,5] , d )

y_bound = d*np.cos(np.pi/6)
x_edge = y_bound*np.cos(np.pi/6)
y_edge = y_bound*np.sin(np.pi/6)

alpha = 3
rho = 1

#Group1
BS1 = HexGrid.activateBS( 1, 1 )#Get BS via row, column
BS2 = HexGrid.activateBS( 0, 1 )#Get BS via row, column
BS3 = HexGrid.activateBS( 2, 0 )#Get BS via row, column
BS4 = HexGrid.activateBS( 1, 0 )#Get BS via row, column

BS1.addSlaveBS( BS2 )
BS1.addSlaveBS( BS3 )
BS1.addSlaveBS( BS4 )

U1 = BS1.addUser([-d,0])
U1_Slave1 = BS2.addUser([-d/2,y_bound])
U1_Slave2 = BS3.addUser([d/2,-y_bound])
U1_Slave3 = BS4.addUser([d,0])

#Group2
BS5 = HexGrid.activateBS( 2, 2 )#Get BS via row, column
BS6 = HexGrid.activateBS( 1, 2 )#Get BS via row, column
BS7 = HexGrid.activateBS( 1, 3 )#Get BS via row, column
BS8 = HexGrid.activateBS( 2, 3 )#Get BS via row, column

BS5.addSlaveBS( BS6 )
BS5.addSlaveBS( BS7 )
BS5.addSlaveBS( BS8 )

U2 = BS5.addUser([d,0])

U2_Slave1 = BS6.addUser([d/2,y_bound])
U2_Slave2 = BS7.addUser([-d,0])
U2_Slave3 = BS8.addUser([-d/2,-y_bound])

#Group3
BS9 = HexGrid.activateBS( 2, 1 )#Get BS via row, column
BS10 = HexGrid.activateBS( 3, 2 )#Get BS via row, column
BS11 = HexGrid.activateBS( 3, 1 )#Get BS via row, column
BS12 = HexGrid.activateBS( 3, 0 )#Get BS via row, column

BS9.addSlaveBS( BS10 )
BS9.addSlaveBS( BS11 )
BS9.addSlaveBS( BS12 )

U3 = BS9.addUser([d/2,y_bound])
U3_Slave1 = BS10.addUser([-d,0])
U3_Slave2 = BS11.addUser([-d/2,-y_bound])
U3_Slave3 = BS12.addUser([d,0])


HexGrid.getNetworkCapacity( alpha )

dpg.start_dearpygui()
dpg.destroy_context()