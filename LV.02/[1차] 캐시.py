def solution(cacheSize, cities):
  ret = 0
  cache = []
  c_index = 0
  if cacheSize == 0:
    return len(cities) * 5

  for i in cities:
    city = i.upper()
    if city in cache:
      cache.remove(city)
      cache.append(city)
      ret += 1
    else:
      ret += 5
      if c_index < cacheSize:
        cache.append(city)
        c_index += 1
      else:
        cache.pop(0)
        cache.append(city)
  return ret