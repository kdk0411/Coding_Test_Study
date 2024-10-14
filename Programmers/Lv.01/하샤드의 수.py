def solution(x):
  answer = False
  ret = 0
  ls = list(map(int, str(x)))
  for i in ls:
    ret += i
  if x % ret == 0:
    answer = True
  return answer