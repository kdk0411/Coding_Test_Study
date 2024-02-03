def solution(arr, k):
  if k % 2 == 0:
    return [i + k for i in arr]
  elif k % 2 != 0:
    return [i * k for i in arr]