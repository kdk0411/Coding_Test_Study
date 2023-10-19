def solution(a, b, c, d):
  answer = 0
  ls = [a, b, c, d] # 입력값을 List로 저장
  arr = list(set(ls)) # List의 중복값 제거 set() 사용

  if len(arr) == 1: # 4가지의 입력값이 모두 같은 경우 -> 중복을 제거한 후 1개의 값만 남은 경우
    answer = int(str(arr[0]) * 4) # arr의 0번째 수를 str로써 4번 곱하여 aaaa와 같은 형태로 만든 후 int화 시킴
  elif len(arr) == 2: # 4가지의 입력값 중 중복되지 않는 값이 2개인 경우 -> 3:1, 2:2의 경우가 있음
    # 주사위 3개가 같은값인 경우 -> 3:1
    if max([ls.count(i) for i in arr]) > 2: # 리스트 내포 문법 -> [표현식 for i in 반복가능 대상] # ls에서 중복된 값이 3회이상 나타나는 경우
      p = max(ls, key=ls.count) # 빈도가 많은 수를 p에 저장
      q = min(ls, key=ls.count) # 빈도가 낮은 수를 q에 저장
      answer = pow(((10 * p) + q), 2) # pow를 이용하여 제곱값을 구함
    # 주사위가 2개씩 같은 경우 -> 2:2
    else:
      answer = ((arr[0] + arr[1]) * abs(arr[0] - arr[1])) # abs를 사용하여 절대값을 추출
  elif len(arr) == 3: # 4개 중 중복을 제외한 값이 3가지인 경우 -> a, a, b, c등의 경우
    p = max(ls, key=ls.count) # 중복되는 값 즉 최빈값을 p에 저장
    tmp = [i for i in arr if i != p] # p와 다른 값을 추출해서 tmp에 저장
    answer = tmp[0] * tmp[1]
  elif len(arr) == 4: # 4개가 모두 다른 경우
    answer = min(arr) # 가장 작은 값을 추출
    
  return answer