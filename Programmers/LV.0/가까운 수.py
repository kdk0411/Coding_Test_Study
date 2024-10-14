def solution(array, n):
  array.sort()
  arr = [abs(n - i) for i in array]
  return array[arr.index(min(arr))]