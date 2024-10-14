def solution(s):
  num = int(len(s) / 2)
  if len(s) % 2 != 0:
    return s[num]
  else:
    return s[num - 1:num + 1]