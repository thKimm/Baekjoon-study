'''
point
1. 인접한 집 못텀
    N에 따른 털리는 집의 최대 -> N//2
    4 2
    5 2
    6 3
    7 3
2. 이게 왜 dp?
'''
def solution(money):
    dp1 = [0] * len(money)
    dp1[0], dp1[1] = money[0], max(money[0], money[1])
    for i in range(2, len(money) - 1):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + money[i])

    dp2 = [0] * len(money)
    dp2[0], dp2[1] = 0, money[1]
    for i in range(2, len(money)):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + money[i])

    return max(max(dp1), max(dp2))