def solution(numbers, target):
    # 재귀 함수 정의 (idx: 현재 탐색 중인 숫자 위치, total: 지금까지의 합계)
    def dfs(idx, total):
        # 모든 숫자를 다 사용했을 때
        if idx == len(numbers):
            # 지금까지의 합이 target과 같으면 1개 방법 찾음, 아니면 0
            return 1 if total == target else 0
        
        # 현재 숫자를 더하는 경우 + 빼는 경우의 수를 합산
        return dfs(idx + 1, total + numbers[idx]) + dfs(idx + 1, total - numbers[idx])

    return dfs(0, 0)