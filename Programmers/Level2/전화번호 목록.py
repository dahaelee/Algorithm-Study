def solution(phone_book):
    phone_book.sort()

    temp = phone_book[0]
    for i in range(1, len(phone_book)):
        if phone_book[i][:len(temp)] == temp:
            return False

    return True