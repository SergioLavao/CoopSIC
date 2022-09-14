import sympy as sym
from UserBase import UserBase

'''Interference as Power Domain Multiplexing (Superposition coding)'''
class UserOMA( UserBase ):

	def __init__( self, BS, alias, relative_position ):
		super().__init__( BS, alias, relative_position )
		self.user_type = 'OMA'
		
	def GetSINR( self, Network, N_0=1, W=1, rho=1, alpha=1 ):
		''' Returns the SINR_IaN of the user using Interference as Noise '''
		numerator = self.BS.Power * self.ChannelFadingGain( self.BS, alpha )		
		denominator = N_0*W*rho
		self.sinr = numerator / denominator
		return ( f'SINR_OMA_{self.alias} = { self.sinr };' )