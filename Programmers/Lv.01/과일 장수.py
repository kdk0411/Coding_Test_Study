def solution(k, m, score):
    score.sort(reverse=True)
    ret = 0
    for i in range(0, len(score), m):
        arr = score[i:i+m]
        if len(arr) == m:
            ret += min(arr) * m
    return ret