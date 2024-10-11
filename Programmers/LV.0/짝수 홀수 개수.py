def solution(num_list):
  left, right = 0, 0
  for i in num_list:
    if i % 2 == 0:
      left += 1
    else:
      right += 1
  return [left, right]