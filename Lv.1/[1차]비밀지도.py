def solution(n, arr1, arr2):
    ret = []
    for i in range(n):
        arr1_b = format(arr1[i], 'b').zfill(n)
        arr2_b = format(arr2[i], 'b').zfill(n)
        tmp = ''
        for j in range(n):
            if arr1_b[j] == '1' or arr2_b[j] == '1':
                tmp += '#'
            else:
                tmp += ' '
        ret.append(tmp)
    return ret
