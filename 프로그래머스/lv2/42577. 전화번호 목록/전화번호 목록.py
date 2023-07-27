def solution(phone_book):
    
    # 1. 오름차순으로 정렬한다.
    phone_book.sort()
    
    for i in range(len(phone_book) - 1):
        n = len(phone_book[i])
        if phone_book[i+1][:n] == phone_book[i]:
            return False
                
    return True