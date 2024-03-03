'''
Point
1. 참여 - 완주 = 완주 X
2. 동명이인 -> set X
3. 단순 remove -> 효율 X
4. 100,000 * 3로 해결
'''
def solution(participant, completion):
    par2cnt = dict()
    for p in participant:
        try:
            par2cnt[p] += 1
        except:
            par2cnt[p] = 1
    for p in completion:
        par2cnt[p] -= 1
    ans = ''
    for p in par2cnt:
        if par2cnt[p] != 0:
            ans = p
    return ans