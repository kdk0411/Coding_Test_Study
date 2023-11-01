def solution(s):
    s = s.split(' ')
    for i in range(len(s)):
        s[i] = s[i].capitalize()
        # capitalize 내장 함수는 첫 문자가 영어일 경우 대문자로 만들고(.title()과 같은 기능) 그외에는 소문자로 만든다.
    return " ".join(s)