def solution(clothes):
    # 1. 종류별 개수를 담을 빈 딕셔너리
    counts = {}

    for name, category in clothes:
        if category in counts:
            counts[category] += 1 # 이미 장부에 있으면 -> 기존 개수에 1을 더해!
        else:
            counts[category] = 1 # 장부에 처음 나온 종류면 -> 1개로 새로 적어!

    # 2. (종류별 개수 + 1)을 모두 곱하기
    answer = 1
    for count in counts.values():
        answer *= (count + 1)

    # 3. 아무것도 안 입은 경우 1가지 빼기
    return answer - 1