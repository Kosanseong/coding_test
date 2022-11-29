import sys

# 회문 문자열: 앞으로 읽으나 뒤로 읽으나 똑같은 것
#sys.stdin = open("input.txt", "r")

n = int(input())
# for i in range(n):
#     s = input()
#     s = s.lower()
#     size = len(s)
#
#     for j in range(size//2):
#         if s[j] != s[-j-1]:
#             print("#%d NO" %(i+1))
#             break
#     else:
#         print("#%d YES" %(i+1))


for i in range(n):
    s = input()
    s = s.lower()
    print(s[::-1]) # 문자열을 reverse 시켜준다.
    if s == s[::-1]:
        print("#%d YES" %(i+1))
    else:
        print("#%d NO" %(i+1))
