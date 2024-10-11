def solution(s):
    p = s.split(' ')
    ret = ''
    for i in p:
        for j in range(len(i)):
            if j%2==0:
                ret += i[j].upper()
            elif j%2!=0:
                ret += i[j].lower()
        ret += ' '
    return ret[0:-1]