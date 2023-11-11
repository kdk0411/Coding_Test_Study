import re
def solution(s):
    ret = []
    arr = s.split(',{')
    # 길이를 기준으로 정렬한다.
    arr.sort(key = len)
    for i in arr:
        # 정규 표현식을 이용해서 \d 즉 숫자만 뽑아내는 것이다. + 한번 이상 반복할때를 의미한다.
        num = re.findall("\d+", i)
        for j in num:
            if int(j) not in ret:
                ret.append(int(j))
    return ret