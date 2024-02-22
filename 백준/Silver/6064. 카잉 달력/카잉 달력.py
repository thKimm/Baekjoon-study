'''
Point
1. 수학

공부
i를 1부터 증가시키면서 계속 증가
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)
def GCD(M,N): # 최대 공약수
    if M % N == 0:
        return N
    else : 
        return GCD(N,M%N)
N = int(input().strip())
for _ in range(N):
    M,N,x,y = list(map(int, input().split()))
    gcd = GCD(M,N)
    Max = int(M*N/gcd)
    X = x
    Y = y
    flag = False
    while X != Y and X <= Max and Y <= Max:
        if X > Y:
            Y += N
        elif X < Y:
            X += M
    print(X if X == Y else -1)