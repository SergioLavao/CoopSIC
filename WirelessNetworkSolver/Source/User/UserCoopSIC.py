import sympy as sym
from UserBase import UserBase

''' Interference as Cooperative SIC '''
class UserCoopSIC ( UserBase ):

	technique = 'CoopSIC'

	sic_slaves = []
	sic_master = None

	isSlave = False

	def __init__( self, BS, alias, relative_position ):
		super().__init__( BS, alias, relative_position )
		self.user_type = 'CoopSIC'
	
	def SetSICMaster( self, sic_master ):
		self.sic_master = sic_master
		self.isSlave = True

	def SetSICSlaves( self, sic_slaves ):
		self.sic_slaves = sic_slaves 
		for slave in sic_slaves:
			slave.SetSICMaster( self )

	def GetSINR( self, Network, N_0=1, W=1, rho=1, alpha=1 ):
		''' Returns the SINR_CoopSIC of the user '''

		sic_master = self.sic_master #Defines the SIC Master User.

		numerator = self.BS.Power * self.ChannelFadingGain( self.BS , alpha )
		
		if self.isSlave:
			numerator = self.BS.Power * sic_master.ChannelFadingGain( self.BS , alpha )
		
		interference = 0
		interferenceInternal = 0

		for BS in Network.BSs: #For every BS in the Network
			if BS.active: #And BS is active
				
				if len( BS.users ) == 0: #Empty BS (Interference source)
					interference = interference + BS.Power * self.ChannelFadingGain( BS , alpha )

				for user in BS.users: #For each user in the BaseStation
					
					BS_interference = 0 #Initialize a new interference source
					BS_interferenceInternal = 0 #Initialize a new interference internal corner MAC

					if user != self: #If user

						BS_interference = BS.Power * self.ChannelFadingGain( BS , alpha )
						
						if self.isSlave: #User has a master
							BS_interference = BS.Power * sic_master.ChannelFadingGain( BS, alpha )
					

					for slave in self.sic_slaves:
						if slave == user:
							BS_interference = 0
							BS_interferenceInternal = BS.Power * self.ChannelFadingGain( BS , alpha )

					interference = interference + BS_interference
					interferenceInternal = interferenceInternal + BS_interferenceInternal


		denominator = (N_0*W*rho) + interference
		denominatorInternal = (N_0*W*rho) + interferenceInternal

		self.sinr = numerator / denominator
		self.sinrInternal = numerator / denominatorInternal

		self.expInternal = f'log2( 1 + { sym.N(self.sinrInternal,3) } );'

		return ( f'SINR_CoopSIC_{self.alias} = { self.sinr }; ' )
