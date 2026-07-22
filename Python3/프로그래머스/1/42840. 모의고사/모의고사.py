def solution(answers):
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    score1 = 0
    score2 = 0
    score3 = 0
    
    for i in range(len(answers)):
        if answers[i] == p1[i % 5]:
            score1 += 1
            
        if answers[i] == p2[i % 8]:
            score2 += 1
            
        if answers[i] == p3[i % 10]:
            score3 += 1
            
    max_score = max(score1, score2, score3)
    
    result = []
    if score1 == max_score:
        result.append(1)
    if score2 == max_score:
        result.append(2)
    if score3 == max_score:
        result.append(3)
        
    return result