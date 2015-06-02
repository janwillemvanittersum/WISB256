from scipy.integrate import odeint
from scipy.linalg import eig
import numpy as np

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
    def df(self,u):
       return np.array([[-self.s, self.s,0],[self.r-u[2],-1,-u[0]],[u[1],u[0],-self.b]])
    def isStable(self,u):
        for i in eig(self.df(u))[0].real:
            if i>=0:
                return False
        return True