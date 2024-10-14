# 최대 공약수를 구하는 함수
def gcd(a, b):
    # a를 b로 나눈 나머지가 0이면 b를 반환
    if a % b == 0:
        return b
    else:
        # 아니면 b와 a를 b로 나눈 나머지의 최대 공약수를 구한다.
        return gcd(b, a % b)

# 인수분해를 하는 함수
def factorization(x):
    d = 2  # 초기 인수
    output = []  # 결과를 담을 리스트

    # 초기 인수가 x보다 작거나 같을 때까지 반복
    while d <= x:
        # x를 d로 나눈 나머지가 0이면,
        if x % d == 0:
            # d를 결과 리스트에 추가하고,
            output.append(d)
            # x를 d로 나눈 몫을 새로운 x로 갱신한다.
            x //= d
        else:
            # 아니면 d를 1 증가시킨다.
            d += 1

    return output  # 결과 리스트 반환

# 주어진 수의 소인수 중 2와 5가 아닌 수가 있는지 확인하는 함수
def solution(a, b):
    # 최대 공약수를 구한다.
    divide_num = gcd(b, a)
    # b를 최대 공약수로 나눈 몫을 구한다.
    result = b // divide_num

    # 몫을 소인수분해하여 소수가 2 또는 5가 아닌 수가 있는지 확인
    for num in factorization(result):
        if num not in [2, 5]:  # 2와 5가 아닌 수가 있다면
            return 0  # 0을 반환
    return 1  # 아니면 1을 반환