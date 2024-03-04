'''
point
1. 인용수 sort
2. 현재 index+1보다 값이 커지면 index+1이 h index 될 수 있음.
'''
def solution(citations):
    answer = 0
    citations.sort()
    paper2cite = {i:0 for i in range(10001)} # key : 인용수, value 논문 권수
    for c in citations:
        paper2cite[c] += 1
    paperWcite = [0]*10001 # index 인용 이상인 논문 개수
    now = len(citations)
    for c in range(10001):
        if paper2cite[c] > 0:
            print(c,paper2cite[c],now)
            paperWcite[c] = now
            now -= paper2cite[c]
        if now <= 0:
            break
    result = list()
    for c in range(10001):
        if paperWcite[c] > 0:
            result.append(min(c,paperWcite[c]))
    answer = max(result)
    return answer