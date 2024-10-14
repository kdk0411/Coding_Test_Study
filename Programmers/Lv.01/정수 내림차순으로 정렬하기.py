def solution(n):
  ls = list(map(int, str(n)))
  ls.sort(reverse=True)
  ret = "".join(str(i) for i in ls)
  return int(ret)