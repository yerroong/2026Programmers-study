class BigNumber(str):
    # 두 문자열을 붙여서 비교 (a + b vs b + a)
    def __lt__(self, other):
        return self + other < other + self

def solution(numbers):
    # 1. 숫자를 custom 클래스(BigNumber)로 바꿉니다.
    numbers = [BigNumber(x) for x in numbers]
    
    # 2. 내장 sort()로 엄청 빠르게 내림차순 정렬 (O(N log N))
    numbers.sort(reverse=True)
    
    # 3. 합쳐서 정답 만들기
    answer = ''.join(numbers)
    
    # 4. 전부 0인 경우 예외 처리
    return '0' if answer[0] == '0' else answer