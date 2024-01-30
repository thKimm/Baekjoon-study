import sys
Ns = int(sys.stdin.readline().strip())
sum = 0
nums = []
num_cnt = dict()
min = 4001
max = -4001
for i in range(Ns):
    N = int(sys.stdin.readline().strip())
    sum += N
    if N > max:
        max = N
    if N < min:
        min = N
    try:
        num_cnt[N] += 1
    except:
        num_cnt[N] = 1
    nums.append(N)
nums.sort()
cnt_num = dict()
Max = 0
for n in list(num_cnt.keys()):
    if Max < num_cnt[n]:
        Max = num_cnt[n]
    try:
        cnt_num[num_cnt[n]].append(n)
    except:
        cnt_num[num_cnt[n]] = [n]
print("{}".format(round(sum/Ns)))
print(nums[Ns//2])
cnt_num[Max].sort()
print(cnt_num[Max][1] if len(cnt_num[Max]) > 1 else cnt_num[Max][0])
print(max-min)