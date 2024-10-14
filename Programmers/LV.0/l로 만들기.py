def solution(myString):
  return ''.join([i if i > 'l' else 'l' for i in myString])