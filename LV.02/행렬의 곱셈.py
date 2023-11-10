def solution(arr1, arr2):
    matrix = [[0]*len(arr2[0]) for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr1[0])):
                matrix[i][j] += arr1[i][k] * arr2[k][j]
    return matrix

def solution_2(A, B):
    return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]