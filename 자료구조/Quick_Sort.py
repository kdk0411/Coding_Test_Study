# 평균적으로 O(n log n)의 시간복잡도를 가지고
# 최악의 경우 O(n^2)의 시간복잡도를 가진다.
def Quick_Sort(arr):
  if len(arr) < 2:
    return arr
  pivot = arr[len(arr)//2] # 중앙에 위치한 값
  left, right, equal = [], [], [] 
  # left : Pivot보다 작은 그룹
  # right : Pivot보다 큰 그룹
  # equal : Pivot과 같은 값
  for i in arr:
    if i < pivot:
      left.append(i)
    elif i > pivot:
      right.append(i)
    elif i == pivot:
      equal.append(i)
  return Quick_Sort(left) + equal + Quick_Sort(right)