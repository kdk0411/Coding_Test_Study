def solution(n, m):
    answer = []
    arr1 = []
    for i in range(1, min(n, m)+1):
        if n%i == 0 and m%i ==0:
            arr1.append(i)
    for i in range(max(n, m), (n*m)+1):
        if i%n == 0 and i%m == 0:
            min_num = i
            break
    max_num = max(arr1)
    answer = [max_num, min_num]
    return answer
# 두 수를 입력받고 1부터 둘 중 작은 수 까지 증가시켜주면서 나눴을 때,
# 동시에 나눠지는 숫자가 있다면 공약수이므로 이를 배열에 담아준다.
# 그 배열중 가장 큰 값이 최대공약수이다.

# 두 수를 입력받고 둘 중 큰 수 부터, 두 수의 곱까지의 숫자를 for문으로 돌면서
# 그 수를 n과 m으로 나웠을때 나머지가 0이라면 그 수가 최소공배수가 된다. 최소인 공배수를
# 구했으니 바로 break로 for문을 탈출하면 된다.