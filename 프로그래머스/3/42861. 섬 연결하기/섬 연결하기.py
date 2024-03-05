'''
point
1. 모든걸 연결 가능하게 하는 하나의 간선만 있으면 됨 -> 최소 신장 트리
2. 비용 존재 -> 크루스칼 알고리즘
    1. 루트 노드 찾기 -> 사이클 발생 확인
    2. 루트 합치기 : 두 원소가 속한 집합을 합침
    edges와 parent 두 리스트로 관리
        parent는 인덱스에 해당하는 노드의 루트 노드를 나타냄
        edges는 (cost, 노드 -> 연결 노드)로 구성하여 cost 별 sort / 루트 노드 탐색 용이하게
'''
def find_parent(parent,x): #x노드의 루트 노드 찾기
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x]) # 루트 노드는 부모 노드를 자기 자신으로 갖고 있는 것 일 것
    return parent[x]

def union_parent(parent,a,b): #연결된 a,b 노드의 루트 노드 합치기
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b: # 루트 노드는 낮은 애로
        parent[b] = a
    else :
        parent[a] = b
    
def solution(n, costs):
    parent = [i for i in range(n)] # 모두 자기 자신으로 초기화
    edges = []
    for C in costs: # edges 초기화
        a,b,c = C
        edges.append((c,a,b))
    edges.sort() # 크루스칼 알고리즘을 위해
    answer = 0
    for edge in edges:
        cost,a,b = edge
        # 사이클이 발생하지 않는 경우에만 포함
        if find_parent(parent,a) != find_parent(parent,b):
            union_parent(parent,a,b)
            answer += cost
    
    return answer