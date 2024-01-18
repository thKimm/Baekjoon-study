import sys
N = int(sys.stdin.readline().strip())
Words = dict()
for i in range(N):
    word = sys.stdin.readline().strip()
    if len(word) in Words:
        if not word in Words[len(word)]:
            Words[len(word)].append(word)
    else:
        Words[len(word)] = [word]
for i in sorted(Words.keys()):
    Words[i].sort()
    for j in Words[i]:
        print(j)