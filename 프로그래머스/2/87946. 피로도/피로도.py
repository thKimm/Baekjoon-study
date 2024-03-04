'''
point
1. 모든 탐색 필요
2. 던전 길이가 짧으니까 ㄱㅊ
'''
from itertools import permutations
def solution(k, dungeons):
    answer = -1
    for i in range(1,1+len(dungeons)):
        permute = permutations(dungeons,i)
        for dungeon in permute:
            K = k
            cnt = 0
            for d in dungeon:
                S,E = d
                if S <= K:
                    K -= E
                    cnt += 1
            answer = max(cnt,answer)
    return answer