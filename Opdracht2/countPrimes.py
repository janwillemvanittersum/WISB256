import sys
import math

path=sys.argv[1]

file=open(path,'r')

pi=0
pi_2=0
prev='-1'
C2 = 0.6601618

for line in file:
    pi+=1
    if int(line)==int(prev)+2:
        pi_2+=1
    prev=line

maxprime=int(prev)
n=maxprime

print('Largest Prime = ',maxprime)
print('-----------------------------------')
print('pi(N)         = ', pi)
print('N/log(N)      = ', n/math.log(n))
print('ratio         = ', pi*math.log(n)/n)
print('-----------------------------------')
print('pi_2(N)       = ', pi_2)
print('2CN/log(N)^2  = ', 2*C2*n/math.log(n)**2)
print('ratio         = ', pi_2*math.log(n)**2/(2*C2*n))