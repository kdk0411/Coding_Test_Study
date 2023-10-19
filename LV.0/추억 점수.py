def solution(name, yearning, photo):
  ret = []
  dic = dict(zip(name, yearning))
  for i in photo:
    cnt = 0
    for j in i:
      cnt += dic.get(j, 0)
    ret.append(cnt)
  return ret
# dict(zip(name, yearning))으로 name과 yearning의 원소들을 딕셔너리로 만든다.
# dic.get(j,0)으로 j에 해당하는 값을 dic에서 찾아와 cnt에 추가한다.
# -> 이는 i를 통해 순서대로 진행 하기 때문에 따로 지정해서 진행할 필요가 없다.

def Solution_Top(이름, 점수, 사진):
  return [sum(점수[이름.index(j)] for j in i if j in 이름) for i in 사진]