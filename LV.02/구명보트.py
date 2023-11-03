def solution(people, limit):
  cnt = 0
  people.sort()
  a, b = 0, len(people) - 1
  while a <= b:
    if people[a] + people[b] <= limit:
      a += 1
    b -= 1
    cnt += 1
  return cnt