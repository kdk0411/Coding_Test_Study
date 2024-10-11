# 문자열 my_string과 두 정수 m, c가 주어집니다.
# my_string을 한 줄에 m 글자씩 가로로 적었을 때 왼쪽부터 세로로 c번째 열에 적힌 글자들을 문자열로 return 하는 solution 함수를 작성해 주세요.
def solution(my_string, m, c):
  tmp = [my_string[i: i+m] for i in range(0, len(my_string), m)]
  # for i in range(0, len(my_string),m)으로 m으로 나눈다.
  # my_string[i: i+m]으로 tmp에 m으로 나누어진 문자열들을 넣는다.
  ret = "".join([tmp[i][c-1] for i in range(0, len(tmp))])
  return ret
