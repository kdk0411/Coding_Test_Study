def solution(numbers):
  cnt = 0
  for i in range(10):
    if i not in numbers:
      cnt += i
  return cnt