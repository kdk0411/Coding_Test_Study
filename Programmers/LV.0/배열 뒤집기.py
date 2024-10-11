def solution(num_list):
  answer = []
  for i in range(len(num_list)):
    let = num_list.pop()
    answer.append(let)
  return answer