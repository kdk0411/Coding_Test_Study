from collections import Counter


def solution(str1, str2):
  str1_lo = str1.lower()
  str2_lo = str2.lower()

  n_str1 = []
  n_str2 = []

  for i in range(len(str1_lo) - 1):
    if str1_lo[i].isalpha() and str1_lo[i + 1].isalpha():
      n_str1.append(str1_lo[i] + str1_lo[i + 1])
  for j in range(len(str2_lo) - 1):
    if str2_lo[j].isalpha() and str2_lo[j + 1].isalpha():
      n_str2.append(str2_lo[j] + str2_lo[j + 1])

  str1_cnt = Counter(n_str1)
  str2_cnt = Counter(n_str2)

  inter = list((str1_cnt & str2_cnt).elements())
  union = list((str1_cnt | str2_cnt).elements())

  if len(union) == 0 and len(inter) == 0:
    return 65536
  else:
    return int(len(inter) / len(union) * 65536)