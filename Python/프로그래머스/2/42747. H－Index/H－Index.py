def solution(citations):
    n = len(citations)
    
    # h를 가장 큰 값(n)부터 0까지 하나씩 줄여가며 확인
    for h in range(n, -1, -1):
        count = 0
        
        # h번 이상 인용된 논문 개수 세기
        for c in citations:
            if c >= h:
                count += 1
                
        # h번 이상 인용된 논문이 h개 이상이면 정답
        if count >= h:
            return h