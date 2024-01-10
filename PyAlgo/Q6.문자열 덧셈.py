def solution(data):
  return sum(map(int, filter(str.isdigit, data)))