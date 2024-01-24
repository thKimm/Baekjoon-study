import sys
N = int(sys.stdin.readline().strip())
members = dict()
for i in range(N):
    age, name = sys.stdin.readline().strip().split()
    age = int(age)
    try:
        members[age].append(name)
    except:
        members[age] = [name]
for i in sorted(members.keys()):
    for j in members[i]:
        print(i, j)