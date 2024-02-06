def solution(num_list):
  sum_1, sum_2 = 0, 0
  for idx, i in enumerate(num_list):
    if (idx + 1) % 2 == 0:
      sum_2 += i
    else:
      sum_1 += i
  return sum_1 if sum_1 > sum_2 else sum_2