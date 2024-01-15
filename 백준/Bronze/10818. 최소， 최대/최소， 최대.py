N=int(input())
number = input().split( )

Number=list()
for n in number:
    Number.append(int(n))

print("{0} {1}".format(min(Number), max(Number)))