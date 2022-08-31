import sys
import numpy as np
import dearpygui.dearpygui as dpg
sys.path.append("./Source")

from HexGridGen import HexGrid

d = 1 #Distance to edge 
x_corner = d*np.cos(np.pi/3)
y_corner = d*np.sin(np.pi/3)

HexGrid = HexGrid( [9,9] , d )

alpha = 3

#SIC Group 1
BS1 = HexGrid.activateBS( 4, 4 )#Get BS via row, column
BS2 = HexGrid.activateBS( 4, 3 )#Get BS via row, column
BS3 = HexGrid.activateBS( 3, 3 )#Get BS via row, column

BS1.addSlaveBS( BS2 )
BS1.addSlaveBS( BS3 )
U1 = BS1.addUser([-d,0])
U1_Slave1 = BS2.addUser([x_corner,-y_corner]),
U1_Slave2 = BS3.addUser([x_corner,y_corner]),


#SIC Group 2
BS4 = HexGrid.activateBS( 2, 2 )#Get BS via row, column
BS5 = HexGrid.activateBS( 1, 3 )#Get BS via row, column
BS6 = HexGrid.activateBS( 1, 2 )#Get BS via row, column

#SIC Group 3
BS7 = HexGrid.activateBS( 3, 0 )#Get BS via row, column
BS8 = HexGrid.activateBS( 2, 1 )#Get BS via row, column
BS9 = HexGrid.activateBS( 2, 0 )#Get BS via row, column

#SIC Group 4
BS7 = HexGrid.activateBS( 0, 4 )#Get BS via row, column
BS8 = HexGrid.activateBS( 1, 4 )#Get BS via row, column
BS9 = HexGrid.activateBS( 0, 5 )#Get BS via row, column

#SIC Group 5
BS7 = HexGrid.activateBS( 2, 5 )#Get BS via row, column
BS8 = HexGrid.activateBS( 3, 5 )#Get BS via row, column
BS9 = HexGrid.activateBS( 3, 6 )#Get BS via row, column

#SIC Group 6
BS7 = HexGrid.activateBS( 4, 1 )#Get BS via row, column
BS8 = HexGrid.activateBS( 5, 1 )#Get BS via row, column
BS9 = HexGrid.activateBS( 5, 2 )#Get BS via row, column


#SIC Group 7
BS7 = HexGrid.activateBS( 6, 3 )#Get BS via row, column
BS8 = HexGrid.activateBS( 7, 3 )#Get BS via row, column
BS9 = HexGrid.activateBS( 7, 4 )#Get BS via row, column

#SIC Group 8
BS7 = HexGrid.activateBS( 6, 5 )#Get BS via row, column
BS8 = HexGrid.activateBS( 5, 5 )#Get BS via row, column
BS9 = HexGrid.activateBS( 6, 6 )#Get BS via row, column

#SIC Group 9
BS7 = HexGrid.activateBS( 4, 7 )#Get BS via row, column
BS8 = HexGrid.activateBS( 5, 7 )#Get BS via row, column
BS9 = HexGrid.activateBS( 5, 8 )#Get BS via row, column

print(f'product_f_rho = {HexGrid.getSystemRhoProduct( alpha, True )}')

dpg.start_dearpygui()
dpg.destroy_context()