'''
point
1. 전체 사전 길이가 5^5 = 3125인 매우 작은 수
2. 완전 탐색
    permutation으로 모든 조합 만들고 sort해보기
    근데 이럼 중복이 안돼서 안됨
    product랑 repeat수로 조절
'''
from itertools import product
def solution(word):
    dictionary = ['A', 'E', 'I', 'O', 'U']
    permute=[]
    for i in range(1,6):
        per = list(product(dictionary,repeat=i))
        permute.extend(list(map(lambda x:''.join(x),per)))
    permute.sort()
    answer=0
    for i in range(len(permute)):
        maybe = ''.join(list(permute[i]))
        if permute[i] == word:
            answer = i+1
            break
    return answer
