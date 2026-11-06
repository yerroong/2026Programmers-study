def solution(nums):
    # 중복을 제거한 폰켓몬 종류의 수
    max_kinds = len(set(nums))
    
    # 내가 고를 수 있는 폰켓몬의 수 (N/2)
    max_select = len(nums) // 2
    
    # 두 값 중 더 작은 값이 최대로 고를 수 있는 폰켓몬 종류의 수
    return min(max_kinds, max_select)