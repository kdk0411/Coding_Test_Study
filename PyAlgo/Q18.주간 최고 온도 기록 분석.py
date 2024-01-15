def solution(data):
  tmp_list = [(tmp, date) for date, tmp in data.items()]
  tmp_list.sort(key=lambda x: (-x[0], x[1]))
  top = tmp_list[:3]
  return [f'{date[2:]}: {tmp}' for tmp, date in top]