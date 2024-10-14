def solution(arr, queries):
  for i in queries:
    ls = [j + 1 for j in arr[i[0]:i[1] + 1]]
    arr[i[0]:i[1] + 1] = ls
  return arr