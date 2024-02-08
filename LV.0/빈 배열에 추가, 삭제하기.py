def solution(arr, flag):
  x = []
  for idx, i in enumerate(arr):
    if flag[idx]:
      for j in range(i * 2):
        x.append(i)
    else:
      for j in range(i):
        x.pop()
  return x