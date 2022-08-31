import numpy as np

#Rho1 = 1 , Rho2 = 1/2
rho1 = 1
rho2 = 1/2

rho1_product = 1.6273922729296484
rho2_product = 0.5003368136743735

print( np.power( rho1_product,(rho2/rho1)) > rho2_product )