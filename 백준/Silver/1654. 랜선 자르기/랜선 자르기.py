import sys
K,N = list(map(int,sys.stdin.readline().split()))

lans = []
for i in range(K):
    lans.append(int(sys.stdin.readline()))

Len = sum(lans)//N
N_ = N
while 1:
    Total = sum([lan//Len for lan in lans])
    if Total >= N:
        break
    N_ += 1   
    Len = sum(lans)//N_
while 1:
    Total = sum([lan//Len for lan in lans])
    if Total < N:
        Len -= 1
        if sum([lan//Len for lan in lans]) >= N:
            break
    if Total >= N:
        Len += 100
print(Len)
    
