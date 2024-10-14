def solution(a, b):
  if a > b:
    a, b = b, a
  elif a == b:
    return a
  return sum(range(a, b + 1))