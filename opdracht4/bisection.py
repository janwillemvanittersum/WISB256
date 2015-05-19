import math

def findRoot(f,a,b,epsilon):
    m=(a+b)/2
    if abs(b-a)<=epsilon:
        return m
    elif f(a)*f(m)<=0:
        return findRoot(f,a,m,epsilon)
    else:
        return findRoot(f,m,b,epsilon)

def findAllRoots(f,a,b,epsilon):
    roots=[]
    totsteps=abs(b-a)/epsilon
    for i in range(0,int(totsteps)):
        if f(a+i*epsilon)*f(a+(i+1)*epsilon)<0:
            roots.append(a+(i+1/2)*epsilon)
    if f(a+int(totsteps)*epsilon)*f(b)<0:
        roots.append((a+b+int(totsteps)*epsilon)/2)
    return roots
