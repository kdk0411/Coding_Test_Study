def solution(data):
  return sorted(data[0], key=lambda x: data[1].get(x.split(' ')[1]))