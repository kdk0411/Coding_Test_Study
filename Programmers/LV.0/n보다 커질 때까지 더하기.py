def solution(numbers, n):
  sum = 0
  for i in numbers:
    if sum <= n:
      sum += i
    elif sum > n:
      return sum
  return sum