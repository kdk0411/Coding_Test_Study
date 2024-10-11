def solution(numlist, n):
  ret = sorted(numlist, key=lambda x: (abs(x - n), n - x))
  return ret