def solution(data):
  return len(list(filter(lambda x: x > 240, map(sum, data))))