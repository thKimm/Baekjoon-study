'''
point
1. m,n 격자점을 올 수 있는 경우의 수
    dmn = dm-1n + dmn+1 두개 오른쪽 아래
    모든 격자점에 대해 진행
'''
def solution(m, n, puddles):
    graph = [[0]*(m+1) for _ in range(n+1)]
    graph[1][1] = 1
    for i in range(1,n+1):
        for j in range(1,m+1):
            if not [j,i] in puddles:
                graph[i][j] += graph[i][j-1]+graph[i-1][j]
        print(*graph[i])
    answer = graph[n][m]%1000000007
    return answer
