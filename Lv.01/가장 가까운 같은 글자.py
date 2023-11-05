def solution(s):
    ret = []
    s_dic = dict()
    for i in range(len(s)):
        if s[i] not in s_dic:
            ret.append(-1)
        else:
            ret.append(i-s_dic[s[i]])
        s_dic[s[i]] = i
    return ret
# s_dic[s[i]] = i 는 같은 글자가 나왔을때 기존 글자의 값을 새로운 값 i로 대체하는 것이다.