def solution(keyinput, board):
  x_lim, y_lim = board[0] // 2, board[1] // 2
  idx = [0, 0]
  for i in keyinput:
    if i == 'left' and idx[0] - 1 >= -(x_lim):
      idx[0] = idx[0] - 1
    elif i == 'right' and idx[0] + 1 <= x_lim:
      idx[0] = idx[0] + 1
    elif i == 'up' and idx[1] + 1 <= y_lim:
      idx[1] = idx[1] + 1
    elif i == 'down' and idx[1] - 1 >= -(y_lim):
      idx[1] = idx[1] - 1
  return idx