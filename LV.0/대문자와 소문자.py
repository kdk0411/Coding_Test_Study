def solution(my_string):
  arr = list(my_string)
  return ''.join([i.lower() if i == i.upper() else i.upper() for i in arr])