def solution(myStr):
  for i in ['a', 'b', 'c']:
    myStr = myStr.replace(i, ' ')
  ret = myStr.split()
  return ret if ret else ["EMPTY"]

def solution_2(myStr):
  for i in 'abc':
    myStr = myStr.replace(i, ' ')
  ret = myStr.split()
  return ret if ret else ["EMPTY"]