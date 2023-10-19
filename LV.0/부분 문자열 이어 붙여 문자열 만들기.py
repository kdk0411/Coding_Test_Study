# 길이가 같은 문자열 배열 my_strings와 이차원 정수 배열 parts가 매개변수로 주어집니다.
# parts[i]는 [s, e] 형태로, my_string[i]의 인덱스 s부터 인덱스 e까지의 부분 문자열을 의미합니다.
# 각 my_strings의 원소의 parts에 해당하는 부분 문자열을 순서대로 이어 붙인 문자열을 return 하는 solution 함수를 작성해 주세요.
def solution(my_strings, parts):
  ret = ''
  for i, j in enumerate(parts):
    ret += my_strings[i][j[0]:j[1] + 1]
  return ret

# enumerate -> Index와 element에 동시 접근이 가능한 함수 이다. 기본적으로 Index와 Element로 이루어진 Tuple을 만들어 준다.
# 따라서 for문을 이용하여 unpaking을 해주어야 한다. enumerate(parts, start=1)으로 시작 지점을 지정 할 수 있다.