def solution(n, lost, reserve):
    # 1. 여벌이 있는데 도난당한 학생을 제외하기
    # (본인이 입어야 하므로 남에게 못 빌려줌)
    new_lost = []
    for l in lost:
        if l in reserve:
            reserve.remove(l) # 빌려줄 수 있는 목록에서 제거
        else:
            new_lost.append(l) # 진짜 빌려야 하는 학생만 남김

    # 순서대로 빌려주기 위해 정렬
    new_lost.sort()
    reserve.sort()

    # 2. 체육복 빌려주기
    # 빌린 학생 수 카운트
    borrowed_count = 0
    
    for l in new_lost:
        # 앞번호 학생에게 먼저 물어보기
        if (l - 1) in reserve:
            reserve.remove(l - 1)
            borrowed_count += 1
        # 뒷번호 학생에게 물어보기
        elif (l + 1) in reserve:
            reserve.remove(l + 1)
            borrowed_count += 1

    # 3. 전체 학생 수 - 도난당한 학생 수 + 빌린 학생 수
    return n - len(new_lost) + borrowed_count