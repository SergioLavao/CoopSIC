#Returns the possible CoopSIC permutations with N Users and n codification order  

N = 3;
n = 2;

Permutations = 0;

#Orden 2
for x in range(1, N + 1):
	for y in range(1, N+1 ):
		if( x != y ):
			Permutations += 1;

#Orden 3
for x in range(1, N + 1):
	for y in range(1, N+1 ):
		if( x != y ):
			for z in range( 1, N + 1):
				if z != y and z!= x:
					Permutations += 1;
					print( x, "->", y, z)