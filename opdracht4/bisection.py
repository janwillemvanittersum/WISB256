import math

def findRoot(f,a,b,epsilon):
    m=(a+b)/2
    if abs(b-a)<=epsilon:
        return m
    elif f(a)*f(m)<=0:
        return findRoot(f,a,m,epsilon)
    else:
        return findRoot(f,m,b,epsilon)