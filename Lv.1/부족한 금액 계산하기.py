def solution(price, money, count):
    ret = 0
    for i in range(1, count+1):
        ret += (price * i)
    if money < ret:
        return ret - money
    else:
        return 0