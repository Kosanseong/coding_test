import sys

sys.stdin = open("input.txt", "r")


def DFS(L):
    global res
    if L == n:
        dif = (max(person) - min(person))
        if res > dif:
            tmp = set()
            for x in person:
                tmp.add(x)
            if len(tmp) == 3:
                res = dif
    else:
        for i in range(len(person)):
            person[i] += a[L]
            DFS(L + 1)
            person[i] -= a[L]


if __name__ == "__main__":
    n = int(input())
    a = list()
    person = [0] * 3
    for _ in range(n):
        a.append(int(input()))
    res = 2147000000
    DFS(0)
    print(res)
