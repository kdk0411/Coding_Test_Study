def solution(progresses, speeds):
  ret = []
  i = 0
  cnt = 0
  while len(progresses) > 0:
    if (progresses[0] + i * speeds[0]) >= 100:
      progresses.pop(0)
      speeds.pop(0)
      cnt += 1
    else:
      if cnt > 0:
        ret.append(cnt)
        cnt = 0
      i += 1
  ret.append(cnt)
  return ret