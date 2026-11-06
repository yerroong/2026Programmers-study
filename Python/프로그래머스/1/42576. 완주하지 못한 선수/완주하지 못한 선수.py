from collections import Counter
def solution(participant, completion):
    new = Counter(participant) - Counter(completion)
    return list(new.keys())[0]