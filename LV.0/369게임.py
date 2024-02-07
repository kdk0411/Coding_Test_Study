def solution(order):
  return sum([1 if i == '3' or i == '6' or i == '9' else 0 for i in str(order)])