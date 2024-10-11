def solution_1(n, left, right):
    arr = [[j for j in range(1, n+1)] for i in range(1, n+1)]
    for i in range(1, n):
        for j in range(arr[0][i]):
          # i번째의 줄에 대해서 접근한다.
          # 0번째에는 1이 1개 1번째에는 2가 2개로 앞을 차례로 채워나가는 방식이다.
          # 때문에 이와같이 arr[0[i] 즉 12345를 22345로 바꾸고
          # 22345를 33345로 바꾸는 형태이다.
            arr[i][j] = arr[0][i]
    arr_2 = [i for il in arr for i in il]
    return arr_2[left:right+1]

# 처음 시도한 방법 이는 시간복잡도를 고려하지 않은 경우이다.

def solution_2(n, left, right):
  arr = []
  for i in range(left, right + 1):
    # left~right까지의 범위를 구한다. 이는 아래와 같이 행렬의 계수를 구하여 하나씩 뽑는 형태이다.
    row = i // n + 1  # 정수 나눗셈을 사용하여 행을 계산합니다.
    col = i % n + 1  # 나머지 연산을 사용하여 열을 계산합니다.
    print("row : ", row, "col : ", col)
    # 최댓값을 계산하고 결과 리스트에 추가합니다.
    max_val = max(row, col)
    # max(row, col) -> 3, 2, 2, 3
    arr.append(max_val)
  return arr
# 두번째로 시도한 경우이다. 이는 이전 방법과 달리 2차원 리스트를 1차원 리스트로 바꾸지 않는 형태이다.
# 리스트의 형태를 바꾸는것은 숫자가 많아질 수록 계산량이 많아지기 때문에 시간초과 현상이 발생한다.
def solution(n, left, right):
  arr = [max((i // n) + 1, (i % n) + 1) for i in range(left, right + 1)]
  return arr
# 마지막으로 최적화 시킨 코드이다.
# 리스트 표현식으로 작성하였으며 내용은 두번째 코드와 동일하다.

solution_2(3,2,5)
