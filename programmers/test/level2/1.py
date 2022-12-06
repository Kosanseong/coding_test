def solution(phone_book):
    answer = True
    phone_book = sorted(phone_book)
    for i in range(len(phone_book) - 1):
        # in을 쓰면 앞이 다른숫자여도 같다고 판단할 가능성이 있음
        if str(phone_book[i+1]).startswith(phone_book[i]):
            return False

    return answer


phone_book = ["1111","21111"]

print("1111" in "21111")

print(solution(phone_book))
