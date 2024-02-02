def solution(rny_string):
  arr = []
  for i in list(rny_string):
    if i == 'm':
      arr.append('rn')
    else:
      arr.append(i)
  return ''.join(arr)