import numpy as np

#Rho1 = 1 , Rho2 = 1/2
rho1 = 1
rho2 = 1/2

rho1_product = 2.3467
rho2_product = 5.403

print( np.power( rho1_product,(rho2/rho1)) > rho2_product )