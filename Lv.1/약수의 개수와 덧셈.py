def solution(left, right):
    answer = []
    ret = 0
    for i in range(left, right+1):
        for j in range(1, i+1):
            if i%j==0:
                answer.append(j)
        if len(answer)%2==0:
            ret += answer[-1]
            answer = []
        else:
            ret -= answer[-1]
            answer = []
    return ret