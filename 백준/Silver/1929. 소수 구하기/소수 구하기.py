import sys
M,N = list(map(int,sys.stdin.readline().split()))

no_primes = set([i for i in range(2,N+1)])

i = 2
while i*i <= N:
    if not i in no_primes:
        pass
    else : 
        no_primes = no_primes - set([i*j for j in range(2,N//i+1)])
    i += 1
ans = list(no_primes)
ans.sort()
for n in ans:
    if n >= M:print(n)
    
