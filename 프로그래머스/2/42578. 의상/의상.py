'''
Point
1. (n+1)*(m+1)...
옷 안입는 경우 (1) + 옷 하나 고르는 경우(n)
'''
def solution(clothes):
    cat2cloth = dict()
    for cloth, cate in clothes:
        try :
            cat2cloth[cate] += 1
        except :
            cat2cloth[cate] = 1
    answer = 1
    for i in cat2cloth:
        answer *= cat2cloth[i]+1
    return answer - 1