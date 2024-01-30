import sys
N = int(sys.stdin.readline().strip())
people = list()
for _ in range(N):
    x,y = list(map(int,sys.stdin.readline().split()))
    people.append(tuple([x,y]))
rank = [1 for i in range(N)]
for i in range(N):
    for j in range(N):
        if i == j:continue
        elif people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            rank[i] += 1
        else : pass
print(*rank)