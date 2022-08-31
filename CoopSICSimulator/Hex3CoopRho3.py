import sys
import numpy as np
import dearpygui.dearpygui as dpg
sys.path.append("./Source")

from HexGridGen import HexGrid

d = 1 #Distance to edge 
x_corner = d*np.cos(np.pi/3)
y_corner = d*np.sin(np.pi/3)

HexGrid = HexGrid( [11,11] , d )

alpha = 3

#SIC Group 1
BS1 = HexGrid.activateBS( 6, 4 )#Get BS via row, column
BS2 = HexGrid.activateBS( 5, 4 )#Get BS via row, column
BS3 = HexGrid.activateBS( 5, 5 )#Get BS via row, column

BS1.addSlaveBS( BS2 )
BS1.addSlaveBS( BS3 )
U1 = BS3.addUser([-d,0])
U1_Slave1 = BS1.addUser([x_corner,-y_corner]),
U1_Slave2 = BS2.addUser([x_corner,y_corner]),

#SIC Group 2
BS4 = HexGrid.activateBS( 6, 0 )#Get BS via row, column
BS5 = HexGrid.activateBS( 6, 1 )#Get BS via row, column
BS6 = HexGrid.activateBS( 5, 1 )#Get BS via row, column

BS4 = HexGrid.activateBS( 8, 2 )#Get BS via row, column
BS5 = HexGrid.activateBS( 8, 3 )#Get BS via row, column
BS6 = HexGrid.activateBS( 7, 3 )#Get BS via row,

BS4 = HexGrid.activateBS( 10, 4 )#Get BS via row, column
BS5 = HexGrid.activateBS( 10, 5 )#Get BS via row, column
BS6 = HexGrid.activateBS( 9, 5 )#Get BS via row,

BS4 = HexGrid.activateBS( 4, 2 )#Get BS via row, column
BS5 = HexGrid.activateBS( 3, 2 )#Get BS via row, column
BS6 = HexGrid.activateBS( 3, 3 )#Get BS via row,

BS4 = HexGrid.activateBS( 8, 6 )#Get BS via row, column
BS5 = HexGrid.activateBS( 7, 6 )#Get BS via row, column
BS6 = HexGrid.activateBS( 7, 7 )#Get BS via row,

BS4 = HexGrid.activateBS( 1, 4 )#Get BS via row, column
BS5 = HexGrid.activateBS( 1, 5 )#Get BS via row, column
BS6 = HexGrid.activateBS( 0, 5 )#Get BS via row,

BS4 = HexGrid.activateBS( 3, 6 )#Get BS via row, column
BS5 = HexGrid.activateBS( 2, 7 )#Get BS via row, column
BS6 = HexGrid.activateBS( 3, 7 )#Get BS via row,

BS4 = HexGrid.activateBS( 5, 8 )#Get BS via row, column
BS5 = HexGrid.activateBS( 5, 9 )#Get BS via row, column
BS6 = HexGrid.activateBS( 4, 9 )#Get BS via row,

print(f'product_f_rho = {HexGrid.getSystemRhoProduct( alpha, True )}')

dpg.start_dearpygui()
dpg.destroy_context()