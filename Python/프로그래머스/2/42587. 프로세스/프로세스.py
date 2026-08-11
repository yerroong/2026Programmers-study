def solution(priorities, location):
    # 1. (우선순위, 원래위치) 형태로 큐(queue) 생성
    queue = [(p, i) for i, p in enumerate(priorities)]
    count = 0  # 몇 번째로 실행되는지 세는 변수

    while queue:
        # 큐의 맨 앞 프로세스를 하나 꺼냄
        cur = queue.pop(0)

        # 큐에 남은 것 중 현재 꺼낸 것보다 우선순위가 높은 게 하나라도 있는지 확인
        if any(cur[0] < item[0] for item in queue):
            # 더 높은 게 있다면 뒤로 다시 보냄
            queue.append(cur)
        else:
            # 실행 가능! 실행 횟수 +1
            count += 1
            # 만약 방금 실행된 프로세스가 우리가 찾던 위치(location)의 프로세스라면 종료
            if cur[1] == location:
                return count