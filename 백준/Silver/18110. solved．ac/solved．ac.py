import sys
def my_round(num):
    if num%1 <0.5:
        return int(num//1)
    else :
        return int(num//1 + 1)
L = int(sys.stdin.readline().strip())
if L == 0:
    print(0)
else:
    del_L = my_round(L*0.15)
    scores = [int(sys.stdin.readline().strip()) for _ in range(L)]
    scores.sort()

    print(my_round(sum(scores[del_L:-del_L])/(L-2*del_L)) if del_L != 0 else my_round(sum(scores)/L))
