from collections import Counter


def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return list(answer.keys())[0]

# def solution(participant, completion):
#     counts = {}

#     for name in participant:
#         if name in counts:
#             counts[name] += 1
#         else:
#             counts[name] = 1

#     for name in completion:
#         counts[name] -= 1

#     for name, count in counts.items():
#         if count > 0:
#             return name

#     return ""