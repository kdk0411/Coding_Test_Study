def solution(my_string, index_list):
  ret = ''
  for i in range(len(index_list)):
    ret += my_string[index_list[i]]
  return ret