
import sys
sys.path.append("./Source")

import numpy as np
import dearpygui.dearpygui as dpg
import sympy as sym

from HexGridGen import HexGrid


N_0, W, rho, alpha = sym.symbols('N_0 W rho alpha')

P1 = sym.Symbol('P1')
P2 = sym.Symbol('P2')

d_edge = 1 #[km]
radius = d_edge/np.cos( np.pi/6 )#Distance to corner[km]
#W = 1
#rho = 1
#alpha = 3
#N_0 = 1

HexGrid = HexGrid( [5,5] , radius )#Create Hex grid network

BS1 = HexGrid.ActivateBS( 1, 1 )#Get BS via row, column
BS1.SetPower( P1 )

BS2 = HexGrid.ActivateBS( 2, 1 )#Get BS via row, column
BS2.SetPower( P2 )

U1 = BS1.AddUser('User1',[0.0,1.0])
U1.SetUserType('PDM')

U2 = BS2.AddUser('User2',[0.0,-1.0])
U2.SetUserType('IaN')

def Python2MatlabExpression( expression ) -> str:
	return expression.replace("**",".^").replace("/","./").replace("*",".*")

print( Python2MatlabExpression( U1.GetSINR( HexGrid, N_0, W, rho, alpha ) ) )
print( Python2MatlabExpression( U2.GetSINR( HexGrid, N_0, W, rho, alpha ) ) )

dpg.start_dearpygui()
dpg.destroy_context()