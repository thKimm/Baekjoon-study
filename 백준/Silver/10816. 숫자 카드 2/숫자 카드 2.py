import sys
N = int(sys.stdin.readline().strip())
Ns_ = list(map(int, sys.stdin.readline().strip().split()))
M = int(sys.stdin.readline().strip())
Ms = list(map(int, sys.stdin.readline().strip().split()))

Ns = dict()
for ns in Ns_:
    try :
        Ns[ns] += 1
    except:
        Ns[ns] = 1

for m in Ms:
    try:
        print(Ns[m], end=' ')
    except:
        print(0, end=' ')