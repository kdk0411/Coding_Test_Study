def solution(i, j, k):
  arr = ''
  for num in range(i, j + 1):
    arr += str(num)
  return list(arr).count(str(k))