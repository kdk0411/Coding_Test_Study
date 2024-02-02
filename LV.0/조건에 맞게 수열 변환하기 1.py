def solution(arr):
  ret = []
  for i in arr:
    if i >= 50 and i % 2 == 0:
      ret.append(i / 2)
    elif i < 50 and i % 2 != 0:
      ret.append(i * 2)
    else:
      ret.append(i)
  return ret