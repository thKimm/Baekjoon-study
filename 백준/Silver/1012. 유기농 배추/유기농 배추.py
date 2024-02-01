import sys
N = int(sys.stdin.readline().strip())
sys.setrecursionlimit(100000) # python recursion 한도는 1000, 2500까지 있을 수 있으니 늘리기
def dfs(X,Y):
    if X < 0 or X >= M or Y < 0 or Y >= N: # 벗어난다면 False
        return False
    if graph[Y][X] == 1:
        graph[Y][X] = 0 # 방문처리
        dfs(X,Y-1) # 인접한 애들에 대해서 모든 노드에 대한 탐색
        dfs(X-1,Y)
        dfs(X,Y+1)
        dfs(X+1,Y)
        return True
    return False



for _ in range(N):
    M,N,K = list(map(int,sys.stdin.readline().split()))
    graph = [[0]*M for i in range(N)]
    for i in range(K):
        m,n = list(map(int,sys.stdin.readline().split()))
        graph[n][m] = 1
    result = 0
    for m in range(M):
        for n in range(N):
            if dfs(m,n): # 모든 노드에 대한 Brute forcing
                result += 1
    print(result)
