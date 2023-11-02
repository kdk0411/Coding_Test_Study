def solution(s):
  s_list = []
  for i in s:
    if len(s_list) == 0:
      s_list.append(i)
    elif s_list[-1] == i:
      s_list.pop()
    else:
      s_list.append(i)
  if len(s_list) == 0:
    return 1
  else:
    return 0
# pop은 맨 마지막것만 빼는 스택 알고리즘인걸 잊지말자