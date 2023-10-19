def solution(absolutes, signs):
  ret = 0
  for i in range(len(absolutes)):
    if signs[i]:
      ret += absolutes[i]
    else:
      ret -= absolutes[i]
  return ret