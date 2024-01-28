def solution(data):
  return all([type(instance).__name__ == class_ for class_, instance in data])