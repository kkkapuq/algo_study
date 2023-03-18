def solution(nums):
    d = dict()
    for n in nums:
        if n not in d:
            d[n] = 1
            continue
        d[n] += 1
    N = len(nums)
    available = len(d.keys())
    if available >= N//2:
        return N//2
    else:
        return available