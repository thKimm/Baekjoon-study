'''
point
1. 연결된 노드 찾기 --> 연결성 판단
2. find parent랑 union parent
3. 루트 노드 개수 조사 # 경로 압축
'''
def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x]) # 자기 자신을 부모 노드로 가지는 노드 찾기
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = parent[a]
    else :
        parent[a] = parent[b]
    
def solution(n, computers):
    # 부모 테이블 갱신
    parent = [i for i in range(n)]
    edge = []
    # union 연산으로 서로소 찾기
    for i in range(n):
        for j in range(n):
            if computers[i][j]:
                union_parent(parent,i,j)
                union_parent(parent,j,i)
    for i in range(n):
        find_parent(parent,i)
    
    answer = len(list(set(parent)))
    return answer