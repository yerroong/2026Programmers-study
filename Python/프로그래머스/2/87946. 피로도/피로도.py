from itertools import permutations

def solution(k, dungeons):
    max_count = 0  # 탐험할 수 있는 최대 던전 수
    
    # 가능한 모든 던전 방문 순서(순열)를 하나씩 확인
    for order in permutations(dungeons):
        current_k = k  # 현재 남아있는 피로도 (매 순서마다 초기화)
        count = 0      # 이번 순서에서 탐험한 던전 수
        
        # 정해진 순서대로 던전을 하나씩 방문
        for need, use in order:
            # 현재 피로도가 최소 필요 피로도 이상인 경우 탐험 가능
            if current_k >= need:
                current_k -= use  # 소모 피로도 차감
                count += 1        # 탐험한 던전 수 증가
            else:
                # 피로도가 부족하면 이 순서에서는 더 이상 진행 불가
                break
        
        # 여태까지 찾은 최댓값과 비교하여 갱신
        if count > max_count:
            max_count = count
            
    return max_count