def solution(players, callings):
  ret = {player: i for i, player in enumerate(players)}
  for i in callings:
    s = ret[i]
    ret[i] -= 1
    ret[players[s - 1]] += 1
    players[s - 1], players[s] = players[s], players[s - 1]
  return players