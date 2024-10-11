def solution_1(array):
  count = [0] * (max(array)+1)

  for i in array:
    count[i] += 1

  F = 0
  for i in count:
    if i == max(count):
      F += 1
  if F > 1:
    return -1
  else:
    return count.index(max(count))

from collections import Counter
def solution_2(array):
  counts = Counter(array)
  mode, max_count = counts.most_common(1)[0]

  if list(counts.values()).count(max_count) > 1:
    return -1
  else:
    return mode