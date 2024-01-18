import sys
N = int(sys.stdin.readline().strip())
Num = []
i = 1
while len(Num) < 10000:
    if "666" in str(i):
        Num.append(i)
    i += 1
Num.sort()
print(Num[N-1])