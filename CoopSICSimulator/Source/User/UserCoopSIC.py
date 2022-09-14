import sympy as sym
from UserBase import UserBase

''' Interference as Cooperative SIC '''
class UserCoopSIC ( UserBase ):

	sic_slaves = []
	sic_master = None

	def __init__( self, BS, alias, relative_position ):
		super().__init__( BS, alias, relative_position )
		self.user_type = 'CoopSIC'
	
	def SetSICMaster( self, sic_master ):
		self.sic_master = sic_master

	def SetSICSlaves( self, sic_slaves ):
		self.sic_slaves = sic_slaves 
		for slave in sic_slaves:
			slave.SetSICMaster( self )

	def GetSINR( self, Network, N_0=1, W=1, rho=1, alpha=1 ):
		''' Returns the SINR_IaN of the user using Interference as Noise '''
		
		sic_master = self.sic_master

		numerator = self.BS.Power * self.ChannelFadingGain( self.BS , alpha )
		
		if sic_master:
			numerator = self.BS.Power * sic_master.ChannelFadingGain( self.BS , alpha )
		
		interference = 0

		for BS in Network.BSs:
			if BS.active:
				
				BS_interference = 0

				if BS != self.BS:
					BS_interference = BS.Power * self.ChannelFadingGain( BS , alpha )
					if sic_master: #User has a master
						BS_interference = BS.Power * sic_master.ChannelFadingGain( BS, alpha )
					
				for slave in self.sic_slaves:
					if slave.BS == BS:
						BS_interference = 0

				interference = interference + BS_interference
		
		denominator = (N_0*W*rho) + interference

		self.sinr = numerator / denominator

		return ( f'SINR_CoopSIC_{self.alias} = { self.sinr };' )