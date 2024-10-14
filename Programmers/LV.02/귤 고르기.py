from collections import Counter
def solution(k, tangerine):
  ret, num = 0, 0
  cnt = Counter(tangerine)
  # Counter 함수를 이용하여 딕셔너리를 만든 후 각 원소의 개수를 측정
  sort_cnt = sorted(cnt.items(), key=lambda x: x[1], reverse=True)
  # sorted를 이용하여 key값에 따라 역순으로 배치
  for i in sort_cnt:
    # 가장 많은 것을 전체 수용가능한 부분에서 뺀 뒤 남은 자리를 찾아야함
    k -= i[1]
    # 여기서 ret은 cnt와 같이 몇번의 경우의 수인지 측정
    ret += 1
    if k <= 0:
    # k 즉 최대 수용가능한 수가 0보다 작거나 같을때 멈춘다.
      break
  return ret