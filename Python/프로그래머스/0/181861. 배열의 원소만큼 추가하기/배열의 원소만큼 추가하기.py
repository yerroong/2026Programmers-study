def solution(arr):
    return  [i for i in arr 
             for _ in range(i)]

    # X = []
    #     for a in arr:
    #         X.extend([a] * a) # 원소를 풀어서 넣음
    #     return X