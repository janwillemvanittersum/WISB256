from scipy.integrate import odeint
import numpy as np
# from numdifftools import Jacobian

def f2(x,y,z):
    sigma=10
    rho=28
    beta=8/3
    return [sigma*(x-y),x*(rho-z)-y,x*y-beta*z]

class Lorenz(object):
    """"""
    def __init__(self,arg, sigma=10,rho=28, beta=8/3):
        self.pos=arg
        self.s=sigma
        self.r=rho
        self.b=beta
    def f(self,x,t):
        return [self.s*(x[1]-x[0]),x[0]*(self.r-x[2])-x[1],x[0]*x[1]-self.b*x[2]]
    def solve(self,T,dt):
        return odeint(self.f,self.pos,np.arange(0,T,dt))
#    def df(self,u):
#       return Jacobian(f2)

L1 = Lorenz([-1,1,0])
u1 = L1.solve(50,.01)
L2 = Lorenz([-1.001,1.001,.001])
u2 = L2.solve(50,.01)
print(u1[0][0],u2[0][0])

for i in range(0,len(u2)):
    if i%200==0:
        print(u2[i])
