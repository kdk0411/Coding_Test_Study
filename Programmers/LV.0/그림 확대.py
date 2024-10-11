def solution(picture, k):
  ls = []
  for i in picture:
    str = ''
    for j in i:
      str += j * k
    for _ in range(k):
      ls.append(str)
  return ls