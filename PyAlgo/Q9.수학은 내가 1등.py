def solution(data):
  return sorted(data, key=lambda x: x['수'], reverse=True)[0]['이름']