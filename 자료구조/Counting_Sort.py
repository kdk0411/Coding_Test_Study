# 배열
def Counting_Sort_array(array):
  count = [0] * (max(array) + 1)

  for num in array:
    count[num] += 1
  for i in range(1, len(count)):
    count[i] += count[i - 1]

  result = [0] * (len(array))

  for num in array:
    index = count[num]
    result[index - 1] = num
    count[num] -= 1

# 딕셔너리
def Counting_Sort_dic(array):
  count_dict = {}

  for num in array:
    if num in count_dict:
      count_dict[num] += 1
    else:
      count_dict[num] = 1

  result = []

  for num in range(max(array) + 1):
    while num in count_dict and count_dict[num] != 0:
      result.append(num)
      count_dict[num] -= 1