def solution(data):
  sum = 0
  for i in data:
    if i % 3 != 0 and i % 5 != 0:
      sum += i
  return sum