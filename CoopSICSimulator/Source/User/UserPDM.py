import sympy as sym
from UserBase import UserBase

'''Interference as Power Domain Multiplexing (Superposition coding)'''
class UserPDM( UserBase ):

	technique = 'PDM'
	sic_slaves = []

	alpha = 1

	def __init__( self, BS, alias, relative_position ):
		super().__init__( BS, alias, relative_position )
		self.user_type = 'PDM'

	def SetAlpha( self, fraq ):
		self.alpha

	def SetSICSlaves( self, sic_slaves ):
		self.sic_slaves = sic_slaves 

	def GetSINR( self, Network, N_0=1, W=1, rho=1, alpha=1 ):
		''' Returns the SINR_IaN of the user using Interference as Noise '''
		numerator = self.BS.Power * self.ChannelFadingGain( self.BS, alpha )
		interference = 0

		for BS in Network.BSs:
			if BS.active: #and self.BS != BS:

				if len( BS.users ) == 0: #Empty BS (Interference source)
					interference = interference + BS.Power * self.ChannelFadingGain( BS , alpha )

				for user in BS.users: #For each user in the BaseStation
					
					BS_interference = 0 #Initialize a new interference source
					
					if user != self: 
						if BS == self.BS:
							if self.alpha == 1:
								self.alpha = 1/len(BS.users)
							BS_interference = ( self.alpha * BS.Power ) * self.ChannelFadingGain( BS , alpha )
						else:
							BS_interference = BS.Power * self.ChannelFadingGain( BS , alpha )

					for slave in self.sic_slaves:
						if slave == user:
							if slave.BS == self.BS:
								BS_interference = 0
							else:
								print(f'%{user.alias} cannot do PDM with {self.alias} because is located in other BS!')

					interference = interference + BS_interference
		
		denominator = (N_0*W*rho) + interference

		self.sinr = numerator / denominator

		return ( f'SINR_PDM_{self.alias} = { self.sinr };' )