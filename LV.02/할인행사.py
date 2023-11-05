from collections import Counter
def solution(want, number, discount):
    cnt = 0
    dic = {}
    for w, n in zip(want, number):
        dic[w] = n
    for i in range(len(discount)-9):
        c = Counter(discount[i:i+10])
        if c == dic:
            cnt+=1
    return cnt

# 이전 사용했던 Counter 함수를 사용했다.
# Dicktionary를 이용하여 풀이를 했다.
# 이전과 달리 값들이 따로따로 지정되었기 때문에 zip을 이용하여 dic에 합쳐주었다.
# 문제의 조건에서 want는 총 10개까지만 수용하기 때문에 조건문에서 -9를 하여 찾았다.
# 전부 검사하는 것이 아닌 연속이 가능하다면 체크하는 형식이다.
# 그리고 일정 구간의 요소들을 Counter를 이용하여 빈도수를 측정하여 이를 c에 저장한다.
# 마지막으로 c와 dic의 요소들이 같다면 cnt를 증가시키는 형태이다.