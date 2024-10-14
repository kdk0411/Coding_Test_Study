def solution(strArr):
  arr = [len(i) for i in strArr]
  return max([arr.count(i) for i in set(arr)])