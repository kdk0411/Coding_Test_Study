def solution(arr):
  cnt = 0
  ls_1 = arr
  while True:
    ls_2 = []
    for i in ls_1:
      if i >= 50 and i % 2 == 0:
        ls_2.append(int(i / 2))
      elif i < 50 and i % 2 != 0:
        ls_2.append(int(i * 2 + 1))
      else:
        ls_2.append(i)
    ret = all(i == j for i, j in zip(ls_1, ls_2))
    if ret: break
    cnt += 1
    ls_1 = ls_2
  return cnt