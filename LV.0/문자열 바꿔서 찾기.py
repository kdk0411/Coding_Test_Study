def solution(myString, pat):
  str = ''.join(["B" if i == "A" else "A" for i in myString])
  return 1 if pat in str else 0