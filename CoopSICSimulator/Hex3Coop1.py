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


BS4 = HexGrid.activateBS( 2, 5 )#Get BS via row, column
BS5 = HexGrid.activateBS( 3, 5 )#Get BS via row, column
BS6 = HexGrid.activateBS( 3, 6 )#Get BS via row, column

BS7 = HexGrid.activateBS( 4, 1 )#Get BS via row, column
BS8 = HexGrid.activateBS( 5, 1 )#Get BS via row, column
BS9 = HexGrid.activateBS( 5, 2 )#Get BS via row, column

BS10 = HexGrid.activateBS( 4, 1 )#Get BS via row, column
BS11 = HexGrid.activateBS( 5, 1 )#Get BS via row, column
BS12 = HexGrid.activateBS( 5, 2 )#Get BS via row, column

BS13 = HexGrid.activateBS( 3, 1 )#Get BS via row, column
BS14 = HexGrid.activateBS( 4, 2 )#Get BS via row, column
BS15 = HexGrid.activateBS( 3, 2 )#Get BS via row, column

BS13 = HexGrid.activateBS( 3, 4 )#Get BS via row, column
BS14 = HexGrid.activateBS( 2, 4 )#Get BS via row, column
BS15 = HexGrid.activateBS( 2, 3 )#Get BS via row, column

BS13 = HexGrid.activateBS( 1, 6 )#Get BS via row, column
BS14 = HexGrid.activateBS( 2, 6 )#Get BS via row, column
BS15 = HexGrid.activateBS( 1, 5 )#Get BS via row, column

BS13 = HexGrid.activateBS( 7, 2 )#Get BS via row, column
BS14 = HexGrid.activateBS( 6, 2 )#Get BS via row, column
BS15 = HexGrid.activateBS( 6, 1 )#Get BS via row, column

BS13 = HexGrid.activateBS( 5, 3 )#Get BS via row, column
BS14 = HexGrid.activateBS( 6, 3 )#Get BS via row, column
BS15 = HexGrid.activateBS( 6, 4 )#Get BS via row, column

BS13 = HexGrid.activateBS( 4, 5 )#Get BS via row, column
BS14 = HexGrid.activateBS( 5, 5 )#Get BS via row, column
BS15 = HexGrid.activateBS( 5, 4 )#Get BS via row, column


BS13 = HexGrid.activateBS( 4, 6 )#Get BS via row, column
BS14 = HexGrid.activateBS( 5, 6 )#Get BS via row, column
BS15 = HexGrid.activateBS( 7, 1 )#Get BS via row, column


S13 = HexGrid.activateBS( 1, 1 )#Get BS via row, column
BS14 = HexGrid.activateBS( 2, 1 )#Get BS via row, column
BS15 = HexGrid.activateBS( 2, 2 )#Get BS via row, column

BS13 = HexGrid.activateBS( 1, 3 )#Get BS via row, column
BS14 = HexGrid.activateBS( 0, 3 )#Get BS via row, column
BS15 = HexGrid.activateBS( 1, 2 )#Get BS via row, column


BS13 = HexGrid.activateBS( 0, 4 )#Get BS via row, column
BS14 = HexGrid.activateBS( 1, 4 )#Get BS via row, column
BS15 = HexGrid.activateBS( 0, 5 )#Get BS via row, column

print(f'product_f_rho = {HexGrid.getSystemRhoProduct( alpha, True )}')

dpg.start_dearpygui()
dpg.destroy_context()