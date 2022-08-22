import sys
import numpy as np
import dearpygui.dearpygui as dpg
sys.path.append("./Source")

from HexGridGen import HexGrid

d = 1 #Distance to edge 
alpha = 3
rho = 1

HexGrid = HexGrid( [5,5] , d )#Create Hex grid network

BS1 = HexGrid.activateBS( 1, 1 )#Get BS via row, column
BS2 = HexGrid.activateBS( 1, 2 )#Get BS via row, column


U1 = BS1.addUser([d,0])
U1_Slave1 = BS2.addUser([-d,0]),

BS1.addSlaveBS( BS2 )

HexGrid.getNetworkCapacity( alpha )

dpg.start_dearpygui()
dpg.destroy_context()