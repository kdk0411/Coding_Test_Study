def solution(array, commands):
    ret = []
    for i in range(len(commands)):
        arr = array[commands[i][0]-1:commands[i][1]]
        arr.sort()
        ret.append(arr[commands[i][2]-1])
    return ret