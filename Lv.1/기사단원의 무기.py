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
    # count_divisors 함수 정의: 주어진 숫자의 약수 개수를 계산하는 함수
    def count_divisors(num):
        if num in divisor_counts:
            # 이미 계산된 값이 캐싱되어 있다면, 해당 값을 반환
            return divisor_counts[num]
        count = 0
        for i in range(1, int(num**0.5) + 1):
            if num % i == 0:
                # 숫자 num을 i로 나눌 때 나머지가 0인 경우, i는 num의 약수
                # 중복 약수를 피하기 위해 i와 num // i가 같으면 count에 1을 더하고, 다르면 2를 더함
                count += 2 if i != num // i else 1
        divisor_counts[num] = count  # 계산된 약수 개수를 캐싱
        return count

    divisor_counts = {}  # 이미 계산된 약수 개수를 저장할 딕셔너리 초기화
    answer = [count_divisors(i) for i in range(1, number + 1)]  # 1부터 number까지 각 숫자의 약수 개수를 계산하여 리스트에 저장
    answer = [power if count > limit else count for count in answer]  # 약수 개수가 limit보다 큰 경우 power로 대체, 그렇지 않으면 원래 개수 유지
    return sum(answer)  # 리스트에 있는 값들을 모두 더한 결과 반환

