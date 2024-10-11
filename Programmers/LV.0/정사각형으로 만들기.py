def solution(arr):
  ls = []
  row = len(arr)
  col = len(arr[0])

  if row > col:
    for i in arr:
      ls.append(i + [0] * (row - col))
  elif row < col:
    for _ in range(col - row):
      arr.append([0] * col)
    ls = arr
  else:
    ls = arr

  return ls