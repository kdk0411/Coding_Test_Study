def solution(my_string):
  return sum([int(word) for word in list(my_string) if word.isdigit()])