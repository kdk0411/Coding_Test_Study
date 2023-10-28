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
    def count_divisors(num):
        if num in divisor_counts:
            return divisor_counts[num]
        count = 0
        for i in range(1, int(num**0.5) + 1):
            if num % i == 0:
                count += 2 if i != num // i else 1
        divisor_counts[num] = count
        return count

    divisor_counts = {}
    answer = [count_divisors(i) for i in range(1, number + 1)]
    answer = [power if count > limit else count for count in answer]
    return sum(answer)
