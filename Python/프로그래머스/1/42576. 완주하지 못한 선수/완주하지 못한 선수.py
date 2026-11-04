from collections import Counter
def solution(participant, completion):
    result = Counter(participant) - Counter(completion)

    return list(result.keys())[0]

# def solution(participant, completion):
#     participant.sort()
#     completion.sort()
    
#     # 1. 앞에서부터 비교하다가 이름이 다른 순간 그 사람이 탈락자
#     for i in range(len(completion)):
#         if participant[i] != completion[i]:
#             return participant[i]
            
#     # 2. 끝까지 다 똑같다면 참가자의 맨 마지막 사람이 탈락자
#     return participant[-1]