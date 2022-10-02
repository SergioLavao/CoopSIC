import sympy as sym
from UserBase import UserBase

'''Interference as Noise User type'''
class UserIaN( UserBase ):

	technique = 'IaN'

	def __init__( self, BS, alias, relative_position ):
		super().__init__( BS, alias, relative_position )

	def GetSINR( self, Network, N_0=1, W=1, rho=1, alpha=3 ):
		''' Returns the SINR_IaN of the user using Interference as Noise '''
		numerator = self.BS.Power * self.ChannelFadingGain( self.BS, alpha )
		interference = 0
		for BS in Network.BSs:
			if BS.active:
				
				if len( BS.users ) == 0: #Empty BS (Interference source)
					interference = interference + BS.Power * self.ChannelFadingGain( BS , alpha )

				for user in BS.users: #For each user in the BaseStation					
					if user != self: #If not user 
						interference = interference + BS.Power * self.ChannelFadingGain( BS, alpha )
		
		denominator = (N_0*W*rho) + interference

		self.sinr = numerator / denominator

		return ( f'SINR_IaN_{self.alias} = { self.sinr };' )