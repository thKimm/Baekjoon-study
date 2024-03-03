def solution(nums):
    pokets = dict()
    for p in nums:
        try:
            pokets[p] += 1
        except:
            pokets[p] = 1
    answer = len(pokets) if len(pokets) <= int(len(nums)/2) else int(len(nums)/2)
    return answer