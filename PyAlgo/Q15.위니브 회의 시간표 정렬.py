def solution(data):
  def convert_time(time):
    hour, min, ap = time.split(" ")[0].split(":") + time.split(" ")[1:]
    if ap == "PM" and hour != "12":
      hour = str(int(hour) + 12)
    elif ap == "AM" and hour == "12":
      hour = "00"
    return f'{hour}:{min} {ap}'

  return sorted(data, key=convert_time)