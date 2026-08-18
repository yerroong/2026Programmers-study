def solution(clothes):
    closet = {}
    
    for name, category in clothes:
        closet[category] = closet.get(category, 0) + 1
        
    answer = 1
    for count in closet.values():
        answer *= count + 1        
        
    return answer -1 #모두 안 입은 상태 제외 후 반환