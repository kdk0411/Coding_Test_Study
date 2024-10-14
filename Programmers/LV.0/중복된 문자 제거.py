def solution(my_string):
  ret = ''
  for i in my_string:
    if i not in ret:
      ret += i
  return ret