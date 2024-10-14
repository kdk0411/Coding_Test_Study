def solution(rsp):
  arr = list(rsp)
  ret = []
  for i in arr:
    if i == "2":
      ret.append("0")
    elif i == "0":
      ret.append("5")
    elif i == "5":
      ret.append("2")
  return ''.join(ret)