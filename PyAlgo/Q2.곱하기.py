def solution(data):
  mix = 0
  for i in data:
    if mix == 0:
      mix = i
    else:
      mix *= i
  return mix