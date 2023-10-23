def solution(strings, n):
    return sorted(strings, key=lambda x : (x[n],x))

# lambda 함수 이해.