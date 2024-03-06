'''
point
1. sort해도 단어 하나씩 바뀌는건 안됨
2. 그렇다면, 다 조사하면서 차이가 하나인것들을 다 graph 연결
3. BFS로 찾기
4. 만약 cnt가 words의 길이를 넘었거나 target이 word에 없으면 0 제출
'''

def solution(begin, target, words):
    graph = [[] for _ in range(len(words)+1)] # 처음은 begin
    if not target in words:
        return 0
    wordsWbegin = [begin] + words
    for i in range(len(wordsWbegin)):
        for j in range(i+1,len(wordsWbegin)):
            cnt = 0
            for k in range(len(wordsWbegin[i])):
                if wordsWbegin[i][k] != wordsWbegin[j][k]:
                    cnt += 1
            if cnt == 1:
                graph[i].append(j)
                graph[j].append(i)
    from collections import deque
    q = deque()
    q.append((0,[]))
    flag = True
    while q:
        if cnt > len(words):
            flag = False
            break
        v,word = q.popleft()
        if wordsWbegin[v] == target:
            break
        for i in graph[v]:
            q.append((i,word+[wordsWbegin[v]]))
    return len(word)
