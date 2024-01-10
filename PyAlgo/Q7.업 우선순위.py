def solution(data):
  return list(map(lambda x: x[0], sorted(data, key=lambda x: x[1])))