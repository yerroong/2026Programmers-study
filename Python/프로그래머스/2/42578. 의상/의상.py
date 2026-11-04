from collections import Counter

def solution(clothes):
    counts = Counter(c for n,c in clothes)
    
    answer = 1
    for i in counts.values():
        answer = answer*(i+1)
    return answer-1