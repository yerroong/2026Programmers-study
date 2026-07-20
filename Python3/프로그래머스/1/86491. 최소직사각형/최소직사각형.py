def solution(sizes):
    answer = 0

    width = 0
    height = 0

    for w, h in sizes: #
        width = max(width, max(w, h))
        #max(w, h)는 긴 변. 앞에 width는 이전 최대값을 저장하는 
        
        height = max(height, min(w, h))
        #min(w, h)는 짧은 변. 앞에 height는 이전 최대값을 저장하는 

    answer = width * height

    return answer