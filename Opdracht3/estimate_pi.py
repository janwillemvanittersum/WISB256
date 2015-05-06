import random
import math
import sys

def drop_needle(l):
    x0 = random.random()
    a = random.vonmisesvariate(0,0)
    xeind = x0+l*math.cos(a)
    if xeind <0 or xeind >1:
        return True
    else:
        return False

if len(sys.argv)!=3 and len(sys.argv)!=4:
    print('Use: python estimate_pi.py N L')
    exit()
#elif float(sys.argv[2])>1:
#    print('AssertionError: L should be smaller than 1')
#    exit()
elif len(sys.argv)==4:
    seet=int(sys.argv[3])
    random.seed(seet)

N=int(sys.argv[1])
L=float(sys.argv[2])

count=0
for i in range(0, N):
    if drop_needle(L):
        count+=1

p=count/N
if L<=1:
    pi=2*L/p
else:
    pi=2*L/(p-1)-2/(p-1)*(math.sqrt(L**2-1)+math.asin(1/L))

print(count,'hits in',N,'tries')
print('Pi =', pi)