
class Vector(object):
    """Represents a vector in \mathbb{R}^n"""
    def __init__(self,n,c=0.0):
        if isinstance(c, list):
            self.v=[]
            for i in range(0,n):
                self.v.append(c[i])
        else:
            self.v=[c]*n
    def __str__(self):
        ans=''
        for i in range(0,len(self.v)):
            ans+=str(self.v[i])+'\n'
        return ans
    def lincomb(self, other, alpha, beta):
        ans=[]
        for i in range(0,len(self.v)):
            ans.append(alpha*self.v[i]+beta*other.v[i])
        return Vector(len(self.v),ans)
    def scalar(self, alpha):
        return self.lincomb(self,alpha,0)
    def inner(self,other):
        ans=0
        for i in range(0,len(self.v)):
            ans+=self.v[i]*other.v[i]
        return ans
    def norm(self):
        return self.inner(self)**(1/2)

def proj(u,v):
    return u.scalar(v.inner(u)/u.inner(u))

def GrammSchmidt(V):
    for i in range(0,len(V)):
        for j in range(0,i):
            V[i]=V[i].lincomb(proj(V[j],V[i]),1,-1)
        V[i]=V[i].scalar(1/V[i].norm())
    return V


