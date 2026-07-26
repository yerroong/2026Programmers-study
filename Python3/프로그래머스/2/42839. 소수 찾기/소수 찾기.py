def solution(numbers):
    S = set() # 조합된 숫자를 담을 집합 (Set)
    v = [False] * len(numbers) # 방문 여부 (Visited)

    # 1. 숫자 조합 만들기
    def dfs(s):
        if s:
            S.add(int(s))
        for i in range(len(numbers)):
            if not v[i]:
                v[i] = True
                dfs(s + numbers[i])
                v[i] = False

    dfs("")

    # 2. 소수 개수 세기
    ans = 0 # 정답 개수 (Answer)
    for n in S:
        if n < 2:
            continue
            
        is_p = True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                is_p = False
                break
                
        if is_p:
            ans += 1

    return ans