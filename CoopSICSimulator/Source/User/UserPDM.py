import sympy as sym
from UserBase import UserBase

'''Interference as Power Domain Multiplexing (Superposition coding)'''
class UserPDM( UserBase ):

	sic_slaves = []

	def __init__( self, BS, alias, relative_position ):
		super().__init__( BS, alias, relative_position )
		
	def SetSICSlaves( self, sic_slaves ):
		self.sic_slaves = sic_slaves 

	def GetSINR( self, Network, N_0=1, W=1, rho=1, alpha=1 ):
		''' Returns the SINR_IaN of the user using Interference as Noise '''
		numerator = self.BS.Power * self.ChannelFadingGain( self.BS, alpha )
		interference = 0

		for BS in Network.BSs:
			if BS.active and self.BS != BS:
				
				BS_interference = BS.Power * self.ChannelFadingGain( BS, alpha )
				
				for slave in self.sic_slaves:
					if slave.BS == BS:
						BS_interference = 0

				interference = interference + BS_interference
		
		denominator = (N_0*W*rho) + interference

		self.sinr = numerator / denominator

		return ( f'SINR_PDM_{self.alias} = { self.sinr };' )