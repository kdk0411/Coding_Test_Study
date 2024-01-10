def solution(data):
  sum = 0
  for i in range(len(data)):
    str = data[i]
    sum += int(str[3]) * (i + 1)
  return sum