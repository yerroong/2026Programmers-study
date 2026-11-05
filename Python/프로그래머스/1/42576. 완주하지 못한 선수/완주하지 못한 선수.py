from collections import Counter
def solution(participant, completion):
    participant.sort()
    completion.sort()
    answer = Counter(participant)-Counter(completion)
    return list(answer.keys())[0]