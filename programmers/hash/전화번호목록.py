import collections
phone_book = ["119", "97674223", "1195524421", "1194524421"]


# 앞에만 같아야 함 접두어
def solution(phone_book):
    phone_book = sorted(phone_book)
    answer = True
    for i, j in zip(phone_book, phone_book[1:]):
        print('i: ', i, 'j: ', j)
        if j.startswith(i):
            return False
    return answer


print(solution(phone_book))


