import sys
sys.path.append("./Source")

from WirelessNetworkSolver import *

Network = HexGridNetwork( [3,3], SetRadiusFromEdge( 1 ) )

ActivateTrisec( Network, 1, 0 )

VisualizeNetwork()