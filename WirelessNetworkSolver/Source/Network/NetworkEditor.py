import dearpygui.dearpygui as dpg
from HexGridNetwork import HexGridNetwork

#Network editor (Singleton!): Defines user and base station parameters, returns the analytical results of the network
class NetworkEditor:
	
	network = None
	alias = ''

	def __init__( self, network ):

		self.network = network

		with dpg.group(parent="PrimaryWindow",horizontal=True):
			dpg.add_text(f'BW = {network.W},')
			dpg.add_text(f'rho = {network.rho},')
			dpg.add_text(f'N_0 = {network.N_0},')
			dpg.add_text(f'alpha = {network.alpha}')

	def AddNetworkModel( self , networkAlias ):

		with dpg.collapsing_header(parent="PrimaryWindow",label=f'{networkAlias}'):
			self.alias = networkAlias
			for BS in self.network.BSs:
				for user in BS.users:
						with dpg.group(horizontal=True):
							dpg.add_text(f'{user.alias} at {user.BS.alias} {user.relative_position} using {user.technique}')
							if user.technique == 'OMA':
								dpg.add_text(f' with alpha {user.alpha} ')

							if user.technique == 'CoopSIC':
								if len(user.sic_slaves) > 0:
									dpg.add_text(f' with Slaves = ')
									for slave in user.sic_slaves:
										dpg.add_text(f'{slave.alias}')
										if user.sic_master:
											dpg.add_text(f'Master = {slave.sic_master.alias}')

							if user.technique == 'PDM':
								dpg.add_text(f' with alpha {user.alpha} ')
								if len(user.sic_slaves) > 0:	
									dpg.add_text(f' with Slaves = ')
									for slave in user.sic_slaves:
										if slave.BS != user.BS:
											dpg.add_text(f'{slave.alias}(WARN!)')
										else:
											dpg.add_text(f' {slave.alias}')

		self.GetNetworkExpression()

	def GetNetworkExpression( self ):
		
		capacity = f'{self.alias} = '

		network = self.network

		for BS in network.BSs:
			for user in BS.users:
				userCapacity = self.Python2MatlabExpression( user.GetCapacity( Network=network, N_0=network.N_0, W=network.W, rho=network.rho, alpha=network.alpha ))
				print( userCapacity )
				
				try:
					if user.sinrInternal:
						print( f'{self.alias}_{user.alias}_Internal = {self.Python2MatlabExpression( user.expInternal )}' )
				except Exception as e:
					pass

				capacity = capacity + user.GetUserAliasVariable() + '+'

		capacity = capacity[:-1]

		capacity = capacity +';'
		
		print( capacity )

		network.ClearUsers()

	def Python2MatlabExpression( self, expression ):
		return expression.replace("**",".^").replace("/","./").replace("*",".*").replace("1.0.*","").replace("(1).*","")