def solution(nums):
    num = len(nums)/2
    arr = set(nums)
    if num>len(arr):
        return len(arr)
    else:
        return int(num)