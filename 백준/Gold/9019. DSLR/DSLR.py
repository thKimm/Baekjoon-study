'''
Point
1. 최소횟수 찾기
2. 4개의 연산만
3. 너비 우선 탐색
4. node의 제한은 없는걸로

고민점 : 언제 멈출건가? 
    A == B 인 시점에 종료
    아무거나 출력하면 된댔으니까
'''
import sys
input = sys.stdin.readline
from collections import deque
N = int(input().strip())
for _ in range(N):
    visited = [False]*10000
    A,B = list(map(int,input().split()))
    q = deque()
    
    q.append((A,''))
    visited[A]=True
    while q:
        A,cals = q.popleft()
        if A == B:
            break
        D = (2*A) % 10000
        S = (10000+A-1)%10000
        L = int(str(A%1000)+str(A//1000)) if not A//1000 == 0 else int(str(A%1000)+'0')
        R = int(str(A%10)+str(A//10).zfill(3))
        if not visited[D] : 
            visited[D] = True
            q.append((D,cals+'D'))
        if not visited[S] : 
            visited[S] = True
            q.append((S,cals+'S'))
        if not visited[L] :
            visited[L] = True
            q.append((L,cals+'L'))
        if not visited[R] :
            visited[R] = True
            q.append((R,cals+'R'))
    print(cals)