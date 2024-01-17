import sys
N,M = list(map(int,input().split()))
Nums = list(map(int,input().split()))
Sum_ = [Nums[i] + Nums[j] + Nums[k] for i in range(N) for j in range(N-1) for k in range(N-2) if (i > j) and (j>k)]
Sum_.sort()
Over = [Sum <= M for Sum in Sum_]
if Over[-1] == True:
    print(Sum_[-1])
else:
    Maxidx = Over.index(False)-1
    print(Sum_[Maxidx])