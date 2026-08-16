def solution(name):
    n = len(name)
    
    # 1. 알파벳 변경 횟수 (상하 이동)
    up_down = 0
    for c in name:
        up_down += min(ord(c) - ord('A'), ord('Z') - ord(c) + 1)
        
    # 2. 커서 이동 횟수 (좌우 이동)
    left_right = n - 1  # 단순히 오른쪽으로 계속 이동하는 경우
    
    for i in range(n):
        # i번째 다음부터 연속되는 'A'의 끝 위치 찾기
        next_i = i + 1
        while next_i < n and name[next_i] == 'A':
            next_i += 1
            
        # 꺾어서 이동하는 최단 거리 계산
        turn_right = i * 2 + (n - next_i)
        turn_left = (n - next_i) * 2 + i
        
        left_right = min(left_right, turn_right, turn_left)
        
    return up_down + left_right