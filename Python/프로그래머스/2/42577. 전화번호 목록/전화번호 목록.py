def solution(phone_book):
    phone_book.sort() #sort를 해야지 앞 뒤로 비교 가능
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True