def solution(array, n):
  sum = 0
  for i in array:
    if i == n:
      sum += 1
  return sum