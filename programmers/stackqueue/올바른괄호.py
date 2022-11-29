s = "()()"
s1 = "(())()"
s2 = ")()("
s3 = "(()("


def solution(s):
    arr = []
    answer = False

    for i in range(len(s)):
        if not arr and s[i] == ")":
            return answer
        elif i == 0:
            arr.append(s[i])
        else:
            if s[i] == "(":
                arr.append(s[i])
            elif s[i] == ")" or arr:
                arr.pop()
    if not arr:
        return True

    return answer


print(solution(s3))
