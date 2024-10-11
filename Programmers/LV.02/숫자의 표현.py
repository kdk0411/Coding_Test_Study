def solution(n):
    ret = 0
    for i in range(1, n+1):
        tt = 0
        for j in range(i, n+1):
            tt += j
            if tt==n:
                ret += 1
                break
            elif tt>n:
                break
    return ret