# 데이터가 정렬되어 있는 상태에서 원하는 값을 찾아내는 알고리즘이다.
# 대상 데이터의 중앙값과 찾고자 하는 값을 비교하여 절반씩 줄이며 대산을 찾는다.
# 기능 : 타깃 데이터 탐색
# 특징 : 중앙값 비교를 통한 대상 축소 방식
# 시간 복잡도 : O(logN)

def Binary_search(data, search):
  if len(data) == 1 and data[0] == search:
    return 'Find. {}'.format(search)
  if len(data) == 1 and data[0] != search:
    return 'None'
  if len(data) == 0:
    return 'Not at all.'

  medium = len(data)//2

  if search == data[medium]:
    return 'Find. {}'.format(search)
  else:
    if search > data[medium]:
      return Binary_search(data[medium+1:], search)
    else:
      return Binary_search(data[:medium], search)