def solution(n):
  ls = []
  i = 2
  while i <= n:
    if n % i == 0:
      if i not in ls:
        ls.append(i)
      n //= i
    else:
      i += 1
  return ls