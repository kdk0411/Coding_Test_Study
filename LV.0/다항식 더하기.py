def solution(polynomial):
  arr = polynomial.split()
  x_num = 0
  s_num = 0
  for i in arr:
    if 'x' in i:
      if i[:-1]:
        x_num += int(i[:-1])
      else:
        x_num += 1
    elif i.isdigit():
      s_num += int(i)
  if x_num == 1:
    if s_num > 0:
      return f"x + {s_num}"
    else:
      return f"x"
  elif x_num > 0:
    if s_num > 0:
      return f"{x_num}x + {s_num}"
    else:
      return f"{x_num}x"
  else:
    return f"{s_num}"