def solution(before, after):
  before, after = sorted(before), sorted(after)
  return 1 if before == after else 0