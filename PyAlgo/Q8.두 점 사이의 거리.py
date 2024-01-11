def solution(data):
  min = data[1] - data[0]
  min_List = [data[0], data[1]]
  for i in range(2, len(data)):
    tmp = data[i] - data[i - 1]
    if min > tmp:
      del min_List[:]
      min_List.append(data[i - 1])
      min_List.append(data[i])
      min = tmp
  return min_List