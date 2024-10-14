def solution(arr):
  mi = min(arr)
  arr.remove(mi)
  if not arr:
    return [-1]
  return arr