from itertools import combinations
def solution(nums):
    ret = 0
    for i in combinations(nums, 3):
        s = sum(i)
        bl = True
        for j in range(2, int(s ** 0.5) + 1):
            if s % j == 0:
                bl = False
                break

        if bl is True:
            ret += 1
    return ret