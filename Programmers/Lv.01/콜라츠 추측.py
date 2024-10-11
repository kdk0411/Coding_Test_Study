def solution(num):
  ret = num
  count = 0
  while ret != 1:
    if ret % 2 == 0:
      ret = ret / 2
    else:
      ret = ret * 3 + 1
    count += 1
    if count == 500:
      count = -1
      break
  return count