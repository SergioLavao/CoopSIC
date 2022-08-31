import sys
import numpy as np
import dearpygui.dearpygui as dpg
sys.path.append("./Source")

from HexGridGen import HexGrid

d = 1 #Distance to corner

y_bound = d*np.cos(np.pi/6)
x_edge = y_bound*np.cos(np.pi/6)
y_edge = y_bound*np.sin(np.pi/6)

HexGrid = HexGrid( [8,8] , d )

alpha = 3
rho = 1/3

#Group 1
BS1 = HexGrid.activateBS( 4, 0 )#Get BS via row, column
BS2 = HexGrid.activateBS( 4, 1 )#Get BS via row, column
BS3 = HexGrid.activateBS( 1, 1 )#Get BS via row, column
BS4 = HexGrid.activateBS( 2, 1 )#Get BS via row, column

#Group 3
BS5 = HexGrid.activateBS( 4, 3 )#Get BS via row, column
BS6 = HexGrid.activateBS( 3, 3 )#Get BS via row, column

BS5.changeBSColor( [0,255,255,255], True )
BS6.changeBSColor( [0,255,255,255], True )

BS5.addSlaveBS( BS6 )
U3 = BS5.addUser([0,-y_bound])
U3_Slave = BS6.addUser([0,y_bound])

#Group 4
BS7 = HexGrid.activateBS( 0, 2 )#Get BS via row, column
BS8 = HexGrid.activateBS( 0, 3 )#Get BS via row, column
BS9 = HexGrid.activateBS( 2, 4 )#Get BS via row, column
BS10 = HexGrid.activateBS( 2, 5 )#Get BS via row, column
BS11 = HexGrid.activateBS( 5, 5 )#Get BS via row, column
BS12 = HexGrid.activateBS( 6, 5 )#Get BS via row, column
BS13 = HexGrid.activateBS( 4, 6 )#Get BS via row, column
BS14 = HexGrid.activateBS( 4, 7 )#Get BS via row, column
BS15 = HexGrid.activateBS( 6, 2 )#Get BS via row, column
BS16 = HexGrid.activateBS( 6, 3 )#Get BS via row, column

print(f'product_f_rho = {HexGrid.getSystemRhoProduct( alpha, True )}')

dpg.start_dearpygui()
dpg.destroy_context()