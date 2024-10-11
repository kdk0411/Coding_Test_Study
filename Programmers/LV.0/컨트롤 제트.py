def solution(s):
  s_ls = s.split()
  sum = 0
  for i in range(len(s_ls)):
    if s_ls[i] == 'Z':
      sum -= int(s_ls[i - 1])
    else:
      sum += int(s_ls[i])
  return sum