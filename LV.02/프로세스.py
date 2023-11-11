from collections import deque
def solution(priorities, location):
    ret = []
    # enumerate로 priorities의 각 요소에 인덱스를 부여해서 특징화를 시켜준다.
    que = deque((i,j) for i, j in enumerate(priorities))
    while que:
        arr = que.popleft()
        if que and any(arr[1] < q[1] for q in que):
            que.append(arr)
        else:
            ret.append(arr)
    for i in ret:
        if i[0] == location:
            return ret.index(i)+1

# 새로 알게된 개념
# 1. pop, popleft/ append, appendleft -> 둘다 기본적으로 가장 마지막 인덱스에 추가제거이다. 이것을 반대로 left를 붙여 사용하면
# 첫번째 인덱스의 요소에 접근이 가능하다.
# 2. deque -> 스택 or 큐의 형태로 만든다.
# dq = deque('Hello')로 사용하면 dq에는 ['H', 'e', 'l', 'l', 'o']로 바뀐다.
# 이는 deque로 각 문자가 요소로 된 리스트 형태의 deque가 만들어 지는 것이다.