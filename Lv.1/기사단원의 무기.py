def solution_1(number, limit, power):
    answer = []
    for i in range(1, number+1):
        arr = []
        for j in range(1,i+1):
            if i%j == 0:
                arr.append(j)
        answer.append(len(arr))
    for i in range(len(answer)):
        if answer[i]>limit:
            answer[i] = power
    return sum(answer)


def solution_2(number, limit, power):
    # count_divisors -> n의 약수 계산
    def count_divisors(n):
        cnt = 0
        if n in dit:
            # n이 딕셔너리에 존재하면 그 값을 리턴
            return dit[n]
        for i in range(1, int(n**0.5)+1):
            if n%i == 0:
                # 숫자 n을 i로 나눌 때 나머지가 0인 경우, i는 n의 약수
                # 중복 약수를 피하기 위해 i와 n // i가 같으면 cnt에 1을 더하고, 다르면 2를 더함
                cnt += 2 if i != n//i else 1
        dit[n] = cnt  # 계산된 약수 개수를 저장
        return cnt

    dit = {}  # 이미 계산된 약수 개수를 저장할 딕셔너리 초기화
    ret = [count_divisors(i) for i in range(1, number + 1)]  # 1부터 number까지 각 숫자의 약수 개수를 계산하여 리스트에 저장
    ret = [power if cnt > limit else cnt for cnt in ret]  # 약수 개수가 limit보다 큰 경우 power로 대체, 그렇지 않으면 원래 개수 유지
    return sum(ret)  # 리스트에 있는 값들을 모두 더한 결과 반환

