'''
Point
1. genre += plays
2. genre.sort()
'''
def solution(genres, plays):
    gen2nums = dict()
    genWplays = dict()
    for i in range(len(genres)):
        try:
            gen2nums[genres[i]] += plays[i]
            genWplays[genres[i]].append((plays[i],i))
        except:
            gen2nums[genres[i]] = plays[i]
            genWplays[genres[i]] = [(plays[i],i)]
    gen2nums_ = sorted(gen2nums.items(), key=lambda x:x[1], reverse = True)
    answer = list()
    for g,_ in gen2nums_:
        cnt = 0
        for p in sorted(genWplays[g],key=lambda x:-x[0]):
            answer.append(p[1])
            cnt += 1
            if cnt > 1:
                break
    return answer