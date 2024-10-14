def solution(n):
  ls = list(map(int, str(n)))
  ret = 0
  for i in ls:
    ret += i
  return ret