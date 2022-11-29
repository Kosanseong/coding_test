import sys

sys.stdin = open("input.txt", "r")

word1 = input()
word2 = input()
dic = dict()

for x in word1:
    dic[x] = dic.get(x, 0) + 1 # x가 없으면 0

for x in word2:
    dic[x] = dic.get(x, 0) - 1

if all(dic[x] == 0 for x in dic.keys()):
    print("YES")
else:
    print("NO")
