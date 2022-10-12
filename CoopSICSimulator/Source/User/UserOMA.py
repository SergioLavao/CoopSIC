import sympy as sym
from UserBase import UserBase

class UserOMA( UserBase ):

	technique = 'OMA'

	alpha = 1

	def __init__( self, BS, alias, relative_position ):
		super().__init__( BS, alias, relative_position )
		self.user_type = 'OMA'
	
	def SetAlpha( self , fraq):
		self.alpha = fraq

	def GetSINR( self, Network, N_0=1, W=1, rho=1, alpha=1 ):
		''' Returns the SINR_IaN of the user using Interference as Noise '''
		numerator = self.BS.Power * self.ChannelFadingGain( self.BS, alpha )		
		denominator = N_0*W*rho

		for BS in Network.BSs:
			if BS.active: #and self.BS != BS:

				if len( BS.users ) == 0: #Empty BS (Interference source)
					denominator = denominator + BS.Power * self.ChannelFadingGain( BS , alpha )

		self.sinr = numerator / denominator
		return ( f'SINR_OMA_{self.alias} = { self.sinr };' )

	def GetCapacity( self, Network, N_0=1, W=1, rho=1, alpha=1 ):
		self.GetSINR( Network, N_0, self.alpha*W, rho, alpha )
		return (f'C_{self.user_type}_{self.alias} = ({self.alpha*W*rho})*log2(1 + {sym.N(self.sinr,3)});')
