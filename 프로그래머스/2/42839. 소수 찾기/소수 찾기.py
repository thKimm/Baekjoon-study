'''
point
1. 모든 경우의 수 8! 완전 탐색
2. 모든 경우의 수를 어떻게 찾을거냐?
    탐색? DFS / BFS
    중복된 숫자가 있을 경우 소수를 두번 탐색
3. 만들 수 있는 소수 중 가장 큰 거까지 나열한건 가장 큰 수부터 나열한 애까지만 조사하면 됨 -> 5자리 수 넘어가면 만드는데 너무 오래 걸림
4. 거기 있는 소수들 중 내가 가진 애로 만들 수 있나 조사
5. itertools
'''
from itertools import permutations      
    
def solution(numbers):
    answer = 0
    numbers = list(map(str,numbers))
    candidates = set()
    for i in range(1,1+len(numbers)):
        permute = permutations(numbers,i)
        permute = set(list(map(lambda x:int("".join(x)),permute)))
        candidates |= permute
    for n in candidates:
        if n > 1:
            flag = True
            for i in range(2,int(n**0.5)+1):
                if n%i == 0:
                    flag = False
                    break
            if flag:
                answer += 1
    return answer
