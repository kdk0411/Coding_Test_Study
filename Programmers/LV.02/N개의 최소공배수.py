def solution(arr):
  ret = arr[0]
  for i in arr:
    ret = (i * ret) / gcd(i, ret)
  return ret


def gcd(a, b):
  r = 0
  while b != 0:
    r = a % b
    a, b = b, r
  return a