def solution(data):
  return sorted(list(map(lambda x: x[0], (filter(lambda x: sum(x[1:]) >= 350, data)))))