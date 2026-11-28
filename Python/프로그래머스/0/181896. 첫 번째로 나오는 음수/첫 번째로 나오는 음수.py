def solution(num_list):
    for i, value in enumerate(num_list):
        if value < 0:
            return i
    return -1
