'''
point
1. BFS를 통한 최단경로 찾기
'''
def solution(maps):
    N = len(maps)
    M = len(maps[0])
    from collections import deque
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    q = deque()
    q.append((0,0))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M:
                if maps[nx][ny]==1:
                    maps[nx][ny] = maps[x][y] + 1
                    q.append((nx,ny))
    answer = maps[N-1][M-1] if maps[N-1][M-1] != 1 else -1
    return answer