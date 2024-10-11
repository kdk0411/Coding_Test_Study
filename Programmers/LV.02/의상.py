def solution(clothes):
    # 해시 맵을 초기화합니다.
    hash_map = {}

    # 결과를 저장할 변수를 1로 초기화합니다.
    answer = 1

    # 각 옷과 그 종류를 순회하면서 해시 맵을 업데이트합니다.
    for clothe, type in clothes:
        # 해당 종류(type)의 옷이 이미 해시 맵에 있다면, 개수를 1 증가시킵니다. 없으면 0으로 초기화 후 1 증가시킵니다.
        hash_map[type] = hash_map.get(type, 0) + 1

    # 해시 맵의 각 종류(type)에 대해 반복합니다.
    for type in hash_map:
        # 해당 종류(type)의 옷을 입을 경우의 수를 계산하고, 결과를 answer에 곱합니다.
        answer *= (hash_map[type] + 1)

    # 모든 경우의 수를 다 계산한 후, 아무것도 입지 않는 경우(1)를 빼서 최종 결과를 얻습니다.
    return answer - 1
