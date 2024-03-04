def solution(sizes):
    hor = list()
    ver = list()
    for s in sizes:
        h,v = sorted(s)
        hor.append(h)
        ver.append(v)
    answer = sorted(hor)[-1]*sorted(ver)[-1]
    return answer