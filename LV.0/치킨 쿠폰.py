def solution(chicken):
  ret = 0
  pay = chicken % 10
  cupon = pay // 10
  while chicken >= 10:
    cupon = chicken // 10
    service = chicken % 10
    ret += cupon
    chicken = cupon + service
  return ret