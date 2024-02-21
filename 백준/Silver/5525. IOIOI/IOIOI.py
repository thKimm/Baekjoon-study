'''
Point
1. 이진 탐색

'''
import sys
input = sys.stdin.readline

N = int(input().strip())
M = int(input().strip())
S = 'IO'*N + 'I'
T = input().strip()
result = 0 
for i in range(len(T)-2*N):
    result += int(T[i:i+len(S)] == S)
print(result)