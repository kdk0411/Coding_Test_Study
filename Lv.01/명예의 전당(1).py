def solution(k, score):
    arr = []
    ret = []
    for i in score:
        if len(arr)<k:
            arr.append(i)
        else:
            if min(arr)<i:
                arr.remove(min(arr))
                arr.append(i)
        ret.append(min(arr))
    return ret