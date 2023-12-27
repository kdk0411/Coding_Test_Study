# 오일러 피 함수 P[N]의 정의
# -> 1부터 N까지 범위에서 N과 서로소인 자연수의 개수를 뜻한다.
# -> P[6] : 1~6 범위에서 6과 서로소인 자연수 개수 -> 1, 5 -> 2개
# 서로소 : 공약수가 1 이외에 없는 것 -> 2, 3은 1이외에 공약수가 없다.
# 1. 구하고자 하는 오일러 피의 범위만큼 배열을 자기 자신의 인덱스값으로 초기화한다.
# 2. 2부터 시작, 현재 배열의 값과 인덱스가 같으면(소수일 때) 현재 선택된
#   숫자(K)의 배수에 해당하는 수를 배열에 끝까지 탐색하며 P[i] = P[i] - P[i]/K 연산을 수행한다.(i는 K의 배수)
# 3. 배열의 끝까지 2번을 반복하여 오일러 피 함수를 완성한다.

# 소인수 분해 -> 소인수들을 리스트로 반환
def factorization(x):
  d = 2 # 시작 지점
  factorization = [] # 소인수를 담을 리스트
  while d <= x: # 배열의 끝에 닿았을때 종료
    if x % d == 0: # d가 x의 소인수 일때 append
      factorization.append(d)
      x = x / d
    else: # 소인수가 아니면 다음으로 넘어감
      d += 1
  return factorization

# 오일러 피 함수
def euler_phi(n):
  primes = factorization(n) # 소인수분해를 완료한 리스트
  k = 1
  for p in set(primes):
    k *= p**(primes.count(p)-1) * (p-1) # 오일러 피 공식
  return k