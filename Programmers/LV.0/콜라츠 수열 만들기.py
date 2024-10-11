def solution(n):
  ret = [n]
  while n != 1:
    if n % 2:
      n = n * 3 + 1
    else:
      n //= 2
    ret.append(n)
  return ret