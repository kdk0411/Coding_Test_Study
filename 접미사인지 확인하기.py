# 어떤 문자열에 대해서 접미사는 특정 인덱스부터 시작하는 문자열을 의미합니다.
# 예를 들어, "banana"의 모든 접미사는 "banana", "anana", "nana", "ana", "na", "a"입니다.
# 문자열 my_string과 is_suffix가 주어질 때, is_suffix가 my_string의 접미사라면 1을, 아니면 0을 return 하는 solution 함수를 작성해 주세요.
def solution(my_string, is_suffix):
  return int(my_string.endswith(is_suffix))

# endswith -> endswith(끝나는 문자, start, end)로 사용하여 문자열이 특정문자로 끝나는지 여부 확인이 가능하다. -> True or False
# startwith -> startwith(시작하는 문자, 시작 지점)으로 사용하며 문자열이 특정문자로 시작하는지 여부 확인이 가능하다. -> True or False
# find -> find(찾을 문자, 시작 지점)으로 사용하며 문자열중 특정 문자의 위치를 반환해 준다. 없을 경우 -1 반환