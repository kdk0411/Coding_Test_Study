def solution(brown, yellow):
  tt = brown + yellow
  for col in range(1, tt + 1):
    if (tt / col) % 1 == 0: #
      row = tt / col
      if row >= col and 2 * (row + col) == brown + 4: # 가로의 길이가 세로와 같거나 큰경우, brown의 개수와 2*row+2*col의 수가 일치할 경우 리턴.
        return [row, col]

# brown의 개수는 2*row + 2*col 빼기4(가장자리 중복되는 것)이다.
