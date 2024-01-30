def solution(my_string):
  return my_string.translate({ord(str): None for str in 'aeiou'})