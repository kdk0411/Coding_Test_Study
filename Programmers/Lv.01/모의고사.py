def solution(answers):
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [2, 1, 2, 3, 2, 4, 2, 5]
    arr3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    ret = []
    for i in range(len(answers)):
        # i%len(arr1) -> 각 리스트의 길이만큼 나누어서 계산하는 방법
        if (arr1[i % len(arr1)] == answers[i]):
            score[0] += 1
        if (arr2[i % len(arr2)] == answers[i]):
            score[1] += 1
        if (arr3[i % len(arr3)] == answers[i]):
            score[2] += 1

    for i in range(len(score)):
        if (score[i] == max(score)):
            ret.append(i + 1)
    return ret