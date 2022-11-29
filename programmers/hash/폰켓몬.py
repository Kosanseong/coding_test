def solution(nums):
    answer = 0
    num = set(nums)
    choice = len(nums) / 2

    if len(num) < choice:
        answer = len(num)
    else:
        answer = choice

    return int(answer)


nums = [3, 3, 3, 2, 2, 2]
print(solution(nums))
