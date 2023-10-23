def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i] = chr((ord(s[i]) - ord('A') + n) % 26 + ord('A'))
        elif s[i].islower():
            s[i] = chr((ord(s[i]) - ord('a') + n) % 26 + ord('a'))

    return "".join(s)

# isupper(), islower() -> 문자의 대소문자 구분 함수, 맞다면 True 아니면 False반환
# ord() -> 문자의 유니코드 정수를 반환 -> a -> 97
# chr() -> 정수에 맞는 유니코드 문자 반환 -> 97 -> a
# %26이 없어도 동작은 하지만 z나 Z가 입력되었을때 a나 A로 한바퀴 도는게 불가능함
# 알파벳 총 개수가 26개이기 떄문에 % 26이다.