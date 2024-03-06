'''
point
1. 외곽을 따라 BFS를 통해 최단 거리 계산
2. 외곽은 어떻게 판단?
    무조건 외곽에 있을 수 밖에 없는 지점 (0,0)에서 DFS를 통해 사각형 외곽에 대한 벽을 세우기
    그래프는 0~51이 있다고 가정
    이동하려는 포인트의 사방 중 하나라도 벽이 있어야 이동하도록 만들면 됨
3. 예외 상황 예제 1. (3,5) -> (3,6) 가 불가능
    발생 이유? 거리가 1이라서
    근데 1씩 탐색. 그럼 0.5로 줄여서 탐색
'''
def solution(rectangle, characterX, characterY, itemX, itemY):
    # 그래프 초기 설정
    Max = 0
    for g in rectangle:
        for gg in g:
            Max = max(Max,gg)
    graph=[[0]*(2*Max+2) for _ in range(2*Max+2)] #51*51
    for r in rectangle: # 내부는 0, 모서리는 1로 채움
        x0,y0,x1,y1 = r
        for x in range(2*x0,2*x1+1):
            for y in range(2*y0,2*y1+1):
                if x0<x/2<x1 and y0<y/2<y1:
                    continue
                else :
                    graph[x][y] = 1
    def dfs(x,y):
        if 0<=x<2*Max+2 and 0<=y<2*Max+2:
            if graph[x][y] == 0:
                graph[x][y] = -1
                dfs(x-1,y)
                dfs(x+1,y)
                dfs(x,y-1)
                dfs(x,y+1)
                return True
            return False
        return False
    import sys
    sys.setrecursionlimit(10000000)
    dfs(0,0)
    from collections import deque
    q = deque()
    q.append((2*characterX,2*characterY))
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if graph[nx][ny] == 1:
                if graph[nx][ny-1] == -1 or graph[nx][ny+1] == -1 or graph[nx-1][ny] == -1 or graph[nx+1][ny] == -1 or graph[nx-1][ny-1] == -1 or graph[nx-1][ny+1] == -1 or graph[nx+1][ny-1] == -1 or graph[nx+1][ny+1] == -1:
                    graph[nx][ny] = graph[x][y] + 0.5
                    q.append((nx,ny))
    # for g in graph:
    #     for gg in g:
    #         print("%5s" %str(gg), end = '')
    #     print()
    answer = int(graph[2*itemX][2*itemY])-1
    return answer
print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]],1,3,7,8))