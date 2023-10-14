def solution(park, routes):
  x = 0
  y = 0
  for i in range(len(park)):
    for j in range(len(park[i])):
      if park[i][j] == 'S':
        x, y = j, i
        break

  for route in routes:
    rx = x
    ry = y
    for step in range(int(route[2])):
      if route[0] == 'E' and rx != len(park[0]) - 1 and park[ry][rx + 1] != 'X':
        rx += 1
        if step == int(route[2]) - 1:
          x = rx
      elif route[0] == 'W' and rx != 0 and park[ry][rx - 1] != 'X':
        rx -= 1
        if step == int(route[2]) - 1:
          x = rx
      elif route[0] == 'S' and ry != len(park) - 1 and park[ry + 1][rx] != 'X':
        ry += 1
        if step == int(route[2]) - 1:
          y = ry
      elif route[0] == 'N' and ry != 0 and park[ry - 1][rx] != 'X':
        ry -= 1
        if step == int(route[2]) - 1:
          y = ry
  return [y, x]