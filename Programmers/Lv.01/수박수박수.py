def solution(n):
    answer = ''
    for i in range(n):
        if len(answer)%2 == 0:
            answer += '수'
        elif len(answer)%2 != 0:
            answer += '박'
    return answer