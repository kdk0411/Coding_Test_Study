def Merge_Sort(arr):
  if len(arr) < 2:
    return arr

  mid = len(arr)//2
  left = Merge_Sort(arr[:mid])
  right = Merge_Sort(arr[mid:])

  merged_arr = []
  l = r = 0
  while l < len(left) and r < len(right):
    if left[l] < right[r]:
      merged_arr.append(left[l])
      l += 1
    else:
      merged_arr.append(right[r])
      r += 1

  merged_arr += left[l:]
  merged_arr += right[r:]
  return merged_arr