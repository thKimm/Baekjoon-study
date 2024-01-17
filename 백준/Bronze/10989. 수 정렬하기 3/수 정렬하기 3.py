import sys
import heapq

n_nums = int(sys.stdin.readline().strip())
Num = dict()
for i in range(n_nums):
    a = int(sys.stdin.readline().strip())
    if a in Num:
        Num[a] += 1
    else : Num[a] = 1
nums = list(Num.keys())
nums.sort()
for i in range(len(nums)):
    for j in range(Num[nums[i]]):
        print(nums[i])