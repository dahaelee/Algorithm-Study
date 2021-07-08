def solution(phone_book):
    phone_book.sort()

    # 정렬된 리스트에서 붙어 있는 것들끼리 검사
    for i in range(len(phone_book) - 1):
        plen = len(phone_book[i])
        if phone_book[i] == phone_book[i + 1][:plen]:
            return False

    return True
