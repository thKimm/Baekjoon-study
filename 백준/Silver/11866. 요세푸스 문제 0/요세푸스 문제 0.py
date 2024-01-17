import sys
N,K = map(int,sys.stdin.readline().split())
Peoples = [i+1 for i in range(N)]
Comb = []
for i in range(N):
    for j in range(K):
        Peoples.append(Peoples.pop(0))
    Comb.append(Peoples.pop(-1))
print("<",end='') 
for c in range(len(Comb)-1):
    print(Comb[c],end=', ')
print(f"{Comb[-1]}>")