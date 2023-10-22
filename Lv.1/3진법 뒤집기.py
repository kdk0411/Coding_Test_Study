def solution(n):
    answer = ''

    while n > 0:
        n, re = divmod(n,3)	# n을 3으로 나눈 몫과 나머지를 각가 n과 re에 저장
        answer += str(re) # re를 str으로 answer에 저장
    return int(answer, 3) # 3진법으로 이루어진 answer를 10진법으로 변환

# divmod() : 몫과 나머지를 리턴합니다. 리턴 값이 2개이므로 튜플을 사용합니다.
# int(x, base) : base 진법으로 구성된 str 형식의 수를 10진법으로 변환해 줌