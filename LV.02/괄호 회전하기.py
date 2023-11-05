def Stack(s):
    stack = []
    for i in s:
        if len(stack)==0: stack.append(i)
        else:
            if i==')' and stack[-1]=='(': stack.pop()
            elif i==']' and stack[-1]=='[': stack.pop()
            elif i=='}' and stack[-1]=="{": stack.pop()
            else: stack.append(i)
    return True if len(stack)==0 else False

# 이전 괄호 문제와 유사하게 Stack 알고리즘을 구현하는 것이다.
# s의 i번째 원소가 stack의 마지막 요소와 짝이 된다면 stack의 마지막 요소를 pop하는 Stack 알고리즘이다.
# 총 3가지의 경우가 존재하기 때문에 위와 같이 작성하면 된다.
# 만약 서로 일치 하지 않으면 stack의 마지막에 추가한다.

def solution(s):
    ret = 0
    for i in range(len(s)):
        if Stack(s): ret += 1
        s = s[1:] + s[0]
    return ret

# 처음은 s[0], s[-1] = s[-1], s[0]으로 하려 했지만 생각한것과 달리 리스트를 이런식으로 조작이 불가능했다.
# 따라서 s = s[1:](0번째 요소 이후부터) + s[0](s의 0번째 요소)를 합치는 식으로 한바퀴 돌았다.
#