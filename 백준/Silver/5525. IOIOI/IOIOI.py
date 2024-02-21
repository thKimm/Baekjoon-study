'''
Point
1. 이진 탐색

공부
1. 시간 초과를 피하기 위해선 KMP 알고리즘
'''
import sys
input = sys.stdin.readline

N = int(input().strip())
M = int(input().strip())
S = 'IO'*N + 'I'
T = input().strip()
result = 0 
flag = False
# for i in range(M-2*N):
#     for j in range(2*N+1):
#         if S[j] != T[i+j]:
#             flag = True
#             break
#     result += int(not flag)
#     if not flag:
#         i += 2
#     flag = False
def kmp(all_string, pattern):
    #  kmp_table
    table = [0 for _ in range(len(pattern))]
    i = 0
    for j in range(1, len(pattern)):
        while i > 0 and pattern[i] != pattern[j]:
            i = table[i-1]

        if pattern[i] == pattern[j]:
            i += 1
            table[j] = i

    #  kmp
    result = []
    i = 0
    for j in range(len(all_string)):
        while i > 0 and pattern[i] != all_string[j]:
            i = table[i-1]

        if pattern[i] == all_string[j]:
            i += 1
            if i == len(pattern):
                result.append(j - i + 1)
                i = table[i-1]

    return result
    
print(len(kmp(T,S)))