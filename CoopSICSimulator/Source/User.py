import sympy as sym

import dearpygui.dearpygui as dpg
import numpy as np

class User:

	user_data = None

	relative_position = []
	absolute_position = []

	BS = None

	sinr = 0

	def __init__( self, BS, alias, relative_position ):
		
		self.user_data = {

			"user_alias": alias,
			"type" : "IaN"

		}

		self.BS = BS
		self.relative_position = relative_position
		self.absolute_position = [ BS.position[0] + relative_position[0], BS.position[1] + relative_position[1] ]
		
		if type(relative_position[0]) is float and type(relative_position[1]) is float:
			dpg.draw_circle( center = self.absolute_position, color=[255, 0, 0,255], fill=[255, 0, 0,255],radius=0.07, parent='NetworkPlot' )
			self.plotRay( BS.antenna_absolute_position, [255, 128, 0,50] )
		else:
			dpg.draw_circle( center = BS.antenna_absolute_position, color=[255, 0, 255,255], fill=[255, 0, 255,255],radius=0.07, parent='NetworkPlot' )			

	def SetUserType( self, user_type ):
		self.user_data['type'] = user_type

	def GetSINR( self , Network, N_0, W, rho, alpha) -> str:
		
		alias = self.user_data['user_alias']
		ut = self.user_data['type']

		if ut == 'IaN':
		
			self.GetSINRIaN( Network, N_0, W, rho, alpha )
		
		elif ut == 'PDM':

			self.GetSINRPDM( Network, N_0, W, rho, alpha )
		
		else:
		
			print(f'{alias} has an invalid user_type! assuming IaN...')
			self.GetSINRIaN( Network, N_0, W, rho, alpha )			

		return ( f'SINR_{ut}_{alias} = { self.sinr };' )

	def GetSINRPDM( self , Network, N_0, W, rho, alpha ):
		''' Returns the SINR of the user using Power Domain Multiplexing (SuperpositionCoding-SIC) '''
		numerator = self.BS.Power * sym.Pow( self.DistanceToBS( self.BS ) , -alpha )
		interference = 0
		for BS in Network.BSs:
			if BS.active and self.BS != BS:
				pass

		denominator = (N_0*W*rho) + interference
		self.sinr = numerator / denominator

	def GetSINRIaN( self , Network, N_0, W, rho, alpha ):
		''' Returns the SINR of the user using Interference as Noise '''
		numerator = self.BS.Power * sym.Pow( self.DistanceToBS( self.BS ) , -alpha )
		interference = 0
		for BS in Network.BSs:
			if BS.active and self.BS != BS:
				interference = interference + BS.Power * sym.Pow( self.DistanceToBS( BS ) , -alpha )
		
		denominator = (N_0*W*rho) + interference

		self.sinr = numerator / denominator

	def EuclideanDistance( self, pos1, pos2):
		'''Returns the euclidean distance in the R2 space (positions can be symbolic)'''
		euclidean_distance = sym.sqrt( sym.Pow( pos1[0] - pos2[0], 2 ) + sym.Pow( pos1[1] - pos2[1], 2 ) )
		return euclidean_distance

	def DistanceToBS( self, BS ):
		'''Returns the euclidean distance from the user absolute position to a desired BS antenna.'''
		return ( self.EuclideanDistance( self.absolute_position , BS.antenna_absolute_position  ) )

	def plotRay( self, vec2_to, color ):
		dpg.draw_polygon(parent="NetworkPlot",points=[ self.absolute_position , vec2_to ], color=color, thickness=1 )