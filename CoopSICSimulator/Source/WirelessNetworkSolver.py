import sys
sys.path.append("./Source/User")
sys.path.append("./Source/Network")
sys.path.append("./Source/BaseStation")

from HexGridNetwork import HexGridNetwork

from UserIaN import UserIaN
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

def Python2MatlabExpression( expression ) -> str:
	return expression.replace("**",".^").replace("/","./").replace("*",".*")

def VisualizeNetwork():
	dpg.start_dearpygui()
	dpg.destroy_context()