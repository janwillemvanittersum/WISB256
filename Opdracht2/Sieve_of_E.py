import time
import sys
# sys.argv is a list with the command-line arguments. sysv.arg[0] is the name of Python script

T1 = time.perf_counter()

N=int(sys.argv[1])
path=sys.argv[2]
file=open(path, 'w')

numberlist=N*[True]
numberlist[0]=False
numberlist[1]=False
count=0

for i in range(2,N):
    if numberlist[i]:
        file.write(str(i)+'\n')
        count+=1
        for j in range(2,int((N-1)/i)+1):
            numberlist[i*j]=False

T2 = time.perf_counter()

print('Found '+str(count)+' Prime numbers smaller than '+str(N)+' in '+str(T2-T1)+' sec.')

