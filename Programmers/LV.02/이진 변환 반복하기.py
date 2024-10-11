def solution(s):
    arr = []
    cnt = 0
    rm_cnt = 0
    while True:
        if s == "1":
            break
        rm_cnt += s.count("0")
        s = s.replace("0", '')
        s = bin(len(s))[2:]

        cnt += 1
    arr = [cnt, rm_cnt]
    return arr