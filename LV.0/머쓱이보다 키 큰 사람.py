def solution(array, height):
  sum = 0
  for i in array:
    if i >= height:
      sum += 1
  return sum