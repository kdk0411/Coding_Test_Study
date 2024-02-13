def solution(rank, attendance):
  arr = []
  for i in range(len(rank)):
    if attendance[i]:
      arr.append([rank[i], i])
  arr.sort(key=lambda x: x[0])
  return 10000 * arr[0][1] + 100 * arr[1][1] + arr[2][1]