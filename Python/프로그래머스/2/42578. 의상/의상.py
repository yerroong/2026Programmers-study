def solution(clothes):
    m = {}
    for name, category in clothes:
        if category in m:
            m[category] += 1
        else:
            m[category] = 1
            
    answer = 1        
    for i in m.values():
        answer *= i+1
    return answer -1