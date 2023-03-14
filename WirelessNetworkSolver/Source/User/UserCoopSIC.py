import sympy as sym
from UserBase import UserBase

''' Interference as Cooperative SIC '''
class UserCoopSIC ( UserBase ):

	technique = 'CoopSIC'

	sic_slaves = []
	sic_master = None

	ignore_user = None

	isSlave = False

	def __init__( self, BS, alias, relative_position ):
		super().__init__( BS, alias, relative_position )
		self.user_type = 'CoopSIC'
	
	def SetSICMaster( self, sic_master ):
		self.sic_master = sic_master
		self.isSlave = True

	#SICSlaves( [UserY,UserZ...] ) UserY first decoded, UserZ without UserY interference
	def SetSICSlaves( self, sic_slaves ):
		self.sic_slaves = sic_slaves 
		for slave in sic_slaves:
			slave.SetSICMaster( self )

		N = len(sic_slaves) - 1;
		sic_slaves[N].Ignore(sic_slaves[N - 1])

	def Ignore( self , user ):
		self.ignore_user = user

	def GetSINR( self, Network, N_0=1, W=1, rho=1, alpha=1 ):
		''' Returns the SINR_CoopSIC of the user '''

		sic_master = self.sic_master #Defines the SIC Master User.

		numerator = self.BS.Power * self.ChannelFadingGain( self.BS , alpha )
		IaN_numerator = numerator
		
		if self.isSlave:
			numerator = self.BS.Power * sic_master.ChannelFadingGain( self.BS , alpha )
		
		IaN_interference = 0
		interference = 0
		interferenceInternal = 0

		OCI = 0

		for BS in Network.BSs: #For every BS in the Network
			if BS.active: #And BS is active
				
				if len( BS.users ) == 0: #Empty BS (Interference source)
					interference = interference + BS.Power * self.ChannelFadingGain( BS , alpha )
					OCI = OCI + BS.Power * self.ChannelFadingGain( BS , alpha )

				for user in BS.users: #For each user in the BaseStation
					
					BS_interference = 0 #Initialize a new interference source
					BS_interferenceInternal = 0 #Initialize a new interference internal corner MAC

					BS_IaN_interference = 0

					if user != self: #If user

						BS_interference = BS.Power * self.ChannelFadingGain( BS , alpha )
						BS_IaN_interference = BS_interference
						
						if self.isSlave: #User has a master
							BS_interference = BS.Power * sic_master.ChannelFadingGain( BS, alpha )

						if self.ignore_user == user:
							BS_interference = 0
					
					for slave in self.sic_slaves:
						if slave == user:
							BS_interference = 0
							BS_interferenceInternal = BS.Power * self.ChannelFadingGain( BS , alpha )
							BS_IaN_interference = 0

					IaN_interference = IaN_interference + BS_IaN_interference
					interference = interference + BS_interference
					interferenceInternal = interferenceInternal + BS_interferenceInternal


		IaN_denominator =  (N_0*W*rho) + IaN_interference
		denominator = (N_0*W*rho) + interference
		denominatorInternal = (N_0*W*rho) + interferenceInternal

		self.sinr_IaN =  IaN_numerator / IaN_denominator
		self.sinr = numerator / denominator
		self.sinrInternal = numerator / denominatorInternal

		self.expInternal = f'log2( 1 + { sym.N(self.sinrInternal,3) } );'

		self.OCI = f'OCI_{self.alias} = {sym.N(OCI,3) };';
		return ( f'SINR_CoopSIC_{self.alias} = { self.sinr }; ' )

	def GetCapacity( self, Network, N_0=1, W=1, rho=1, alpha=1 ):
		self.GetSINR( Network, N_0, W, rho, alpha )

		if not self.isSlave:
			return (f'C_{self.user_type}_{self.alias} = ({W*rho})*log2(1 + {sym.N(self.sinr,3)});')
		return (f'C_{self.user_type}_{self.alias} = ({W*rho})*log2(1 + {sym.N(self.sinr_IaN,3)});')
#		return (f'C_{self.user_type}_{self.alias} = min( ({W*rho})*log2(1 + {sym.N(self.sinr,3)}) ,  ({W*rho})*log2(1 + {sym.N(self.sinr_IaN,3)}) );')

	def ClearParameters( self ):
		self.sic_slaves = []
		self.ignore_user = None
		self.sic_master = None
		self.isSlave = False
