def solution(food):
    ret = ''
    for i in range(1,len(food)):
        for j in range(int(food[i]/2)):
            ret += str(i)
    return ret + '0' + ret[::-1]