import numpy as np
from scipy.integrate import odeint
from scipy.integrate import ode
import matplotlib.pylab as plt
import csv



##### Define parameters ########

endpoint = 10000000; # integration range
dx = 1.0; # step size
lam0 = 0.845258; # in unit of omegam, omegam = 3.66619*10^-17
dellam = np.array([0.00003588645221954444, 0.06486364865874367]); # deltalambda/omegam
ks = [1.0,1.0/90]; # two k's
thm = 0.16212913985547778; # theta_m

psi0, x0 = [1.0+0.j, 0.0+0.j], 0 # initial condition
savestep = 100000; # save to file every savestep steps

xlin = np.arange(dx,endpoint+1*dx, dx)

psi = np.zeros([len(xlin)  , 2], dtype='complex_')

xlinsave = np.zeros(len(xlin)/savestep);
psisave = np.zeros([len(xlinsave)  , 2], dtype='complex_')
probsave = np.zeros([len(xlinsave)  , 3])



####### Define the functions required ########

def hamiltonian(x, deltalambda, k, thetam):

    return [[ 0,   0.5* np.sin(2*thetam) * ( deltalambda[0] * np.sin(k[0]*x) + deltalambda[1] * np.sin(k[1]*x) ) * np.exp( 1.0j * ( - x - np.cos(2*thetam) * (  ( deltalambda[0]/k[0] * np.cos(k[0]*x) + deltalambda[1]/k[1] * np.cos(k[1]*x) ) )  ) )     ],   [ 0.5* np.sin(2*thetam) * ( deltalambda[0] * np.sin(k[0]*x) + deltalambda[1] * np.sin(k[1]*x) ) * np.exp( -1.0j * ( - x - np.cos(2*thetam) * ( deltalambda[0] /k[0] * np.cos(k[0]*x) + deltalambda[1] /k[1] * np.cos(k[1]*x) )  ) ), 0 ]]   # Hamiltonian for double frequency

def deripsi(t, psi, deltalambda, k , thetam):

    return -1.0j * np.dot( hamiltonian(t, deltalambda,k,thetam), [psi[0], psi[1]] )

def jac(t, psi, deltalambda, k, thetam):

    return -1.0j * np.array(hamiltonian(t, deltalambda, k, thetam))




############ integrate and save ##########

sol = ode(deripsi,jac).set_integrator('zvode', method='adams', atol=1e-8, with_jacobian=True)
sol.set_initial_value(psi0, x0).set_f_params(dellam,ks,thm).set_jac_params(dellam,ks,thm)

flag = 0
flagsave = 0


while sol.successful() and sol.t < endpoint:
    sol.integrate(xlin[flag])
    if np.mod(flag,savestep)==0:

        probsave[flagsave] = [sol.t, np.absolute(sol.y[1])**2, np.absolute(sol.y[0])**2] # save the probability

        with open(r'assets/probtrans-test-1e7.csv', 'a') as f_handle:
            np.savetxt(f_handle, probsave[flagsave])

        flagsave = flagsave + 1

        print np.absolute(sol.y[1])**2 + np.absolute(sol.y[0])**2 # Check if the solution conserves the total probability
        print np.array(hamiltonian(sol.t,dellam,ks,thm)) # check if the Hamiltonian is Hermitian

    flag = flag + 1



#### Notify at the end######
print "CONGRATS"
