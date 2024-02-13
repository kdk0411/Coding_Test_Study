def solution(n):
  ret = 0
  for i in range(n):
    ret += 1
    while ret % 3 == 0 or '3' in str(ret):
      ret += 1
  return ret