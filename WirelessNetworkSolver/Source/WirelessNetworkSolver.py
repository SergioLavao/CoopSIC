import sys
sys.path.append("../Source/User")
sys.path.append("../Source/Network")
sys.path.append("../Source/BaseStation")
sys.path.append("../Source/NetworkEditor")

from HexGridNetwork import HexGridNetwork
from NetworkEditor import NetworkEditor

from UserIaN import UserIaN
from UserOMA import UserOMA
from UserPDM import UserPDM
from UserCoopSIC import UserCoopSIC

import numpy as np
import sympy as sym
import dearpygui.dearpygui as dpg

def Parameter( alias ):
	return sym.Symbol( alias )

def Parameters( alias ):
	return sym.symbols( alias )

def SetRadiusFromEdge( edge = 1 ) -> float:
	return edge/np.cos( np.pi/6 )

def MatlabExpression( expression ) -> str:
	return expression.replace("**",".^").replace("/","./").replace("*",".*").replace("1.0.*","").replace("(1).*","")
	
def VisualizeNetwork():
	dpg.start_dearpygui()
	dpg.destroy_context()

def GetChannelCombinations( Network ):
	for user in 
	return 

def ActivateTrisec( Network, row , col ):
	
	fixed_row = row
	fixed_col = col

	if row % 2 != 0:
		fixed_col = col + 1
	else:
		fixed_col = col + 1

	if col % 2 != 0:
		fixed_row = row + 1
	else:
		fixed_row = row - 1

	BS1 = Network.ActivateBS( row, col )#Get BS via row, column
	BS2 = Network.ActivateBS( row, fixed_col )#Get BS via row, column
	BS3 = Network.ActivateBS( fixed_row, fixed_col )#Get BS via row, column

	BS1.SetAntennaRelativePosition( [BS1.radius,0.0] )
	BS2.SetAntennaAbsolutePosition( BS1.antenna_absolute_position )
	BS3.SetAntennaAbsolutePosition( BS1.antenna_absolute_position )

	return [BS1, BS2, BS3]


