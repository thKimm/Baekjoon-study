import sys

N = int(sys.stdin.readline().strip())

#an = min(an-1 + 1, an/2,an/3)
D = [0] * (N+1)
for i in range(2,N+1):
    D[i] = D[i-1] + 1 # +1
    D3 = 1e7
    D2 = 1e7
    if i % 3 == 0:
        D3 = min(D[i],D[i//3] + 1)
    if i % 2 == 0:
        D2 = min(D[i],D[i//2] + 1)
    D[i] = min(D2,D3,D[i])
print(D[N])