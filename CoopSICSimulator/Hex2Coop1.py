import sys
import numpy as np
import dearpygui.dearpygui as dpg
sys.path.append("./Source")

from HexGridGen import HexGrid

d = 1 #Distance to corner

y_bound = d*np.cos(np.pi/6)
x_edge = y_bound*np.cos(np.pi/6)
y_edge = y_bound*np.sin(np.pi/6)

HexGrid = HexGrid( [6,6] , d )

alpha = 2
rho = 1

#Group 1
BS1 = HexGrid.activateBS( 0, 0 )#Get BS via row, column
BS2 = HexGrid.activateBS( 0, 1 )#Get BS via row, column
BS3 = HexGrid.activateBS( 1, 0 )#Get BS via row, cbolumn
BS4 = HexGrid.activateBS( 1, 1 )#Get BS via row, column
BS5 = HexGrid.activateBS( 2, 0 )#Get BS via row, column
BS6 = HexGrid.activateBS( 2, 1 )#Get BS via row, column
BS7 = HexGrid.activateBS( 3, 2 )#Get BS via row, column
BS8 = HexGrid.activateBS( 3, 3 )#Get BS via row, column

#Central
BS9 = HexGrid.activateBS( 2, 2 )#Get BS via row, column
BS10 = HexGrid.activateBS( 2, 3 )#Get BS via row, column

BS9.addSlaveBS( BS10 )
U = BS9.addUser([x_edge,y_edge])
U_Slave = BS10.addUser([-x_edge,-y_edge])

BS9.changeBSColor( [0,255,255,255], True )
BS10.changeBSColor( [0,255,255,255], True )

#Group 6
BS11 = HexGrid.activateBS( 4, 4 )#Get BS via row, column
BS12 = HexGrid.activateBS( 4, 5 )#Get BS via row, column
BS13 = HexGrid.activateBS( 3, 4 )#Get BS via row, column
BS14 = HexGrid.activateBS( 3, 5 )#Get BS via row, column
BS15 = HexGrid.activateBS( 2, 4 )#Get BS via row, column
BS16 = HexGrid.activateBS( 2, 5 )#Get BS via row, column
BS17 = HexGrid.activateBS( 1, 2 )#Get BS via row, column
BS18 = HexGrid.activateBS( 1, 3 )#Get BS via row, column

BS11 = HexGrid.activateBS( 3, 0 )#Get BS via row, column
BS12 = HexGrid.activateBS( 3, 1 )#Get BS via row, column
BS13 = HexGrid.activateBS( 4, 2 )#Get BS via row, column
BS14 = HexGrid.activateBS( 4, 3 )#Get BS via row, column
BS15 = HexGrid.activateBS( 0, 2 )#Get BS via row, column
BS16 = HexGrid.activateBS( 0, 3 )#Get BS via row, column
BS17 = HexGrid.activateBS( 1, 4 )#Get BS via row, column
BS18 = HexGrid.activateBS( 1, 5 )#Get BS via row, column

print(f'product_f_rho = {HexGrid.getSystemRhoProduct( alpha, True )}')

dpg.start_dearpygui()
dpg.destroy_context()