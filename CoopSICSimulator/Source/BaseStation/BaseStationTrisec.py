def activateTrisec( self, row , col ):
	
	fixed_row = row
	fixed_col = col

	if row % 2 != 0:
		fixed_col = col + 1
	else:
		fixed_col = col + 1

	if col % 2 != 0:
		fixed_row = row + 1
	else:
		fixed_row = row - 1

	BS1 = self.activateBS( row, col )#Get BS via row, column
	BS2 = self.activateBS( row, fixed_col )#Get BS via row, column
	BS3 = self.activateBS( fixed_row, fixed_col )#Get BS via row, column

	BS1.setMainTrisecAntenna()
	BS2.setTrisecAntenna( BS1 )
	BS3.setTrisecAntenna( BS1 )

	return [BS1, BS2, BS3]