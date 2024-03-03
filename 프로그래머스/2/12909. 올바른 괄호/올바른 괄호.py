'''
Point
1. 이전엔 재귀로 푼 문제
2. 재귀로 다음 짝이 어디있나 찾도록. 제일 가까운 짝이 안맞으면 False 맞으면 True
3. 이걸 스택, 큐로....
4. LIFO 스택 구조
    (는 계속 넣다가
    )가 나오면 
    제일 마지막에 있는 애랑 비교할건데, 비어있으면 False
'''
def solution(s):
    answer = True
    strs = list()
    for c in s:
        if c == "(":
            strs.append(c)
        else :
            if len(strs) == 0:
                answer = False
                break
            else:
                strs.pop()
    if len(strs) != 0:
        answer = False            
    return answer