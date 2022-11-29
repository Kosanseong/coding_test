import sys

sys.stdin = open("input.txt", "r")


# 부모 왼쪽 오른쪽은 -> 전위순회
# 왼쪽 부모 오른쪽은 -> 중위순회
# 왼쪽 오른쪽 부모는 -> 후위순
# 부모 노드 값에 부모x2 하면 왼쪽 부모x2+1를 하면 오른쪽 자식식

def DFS(v):
    if v > 7:
        return
    else:
        print(v, end=' ') # 함수 본연의 일이라면 호출전에는 이러면 전위 순회 -> 거의 대부분
        DFS(v * 2)
        print(v, end=' \n') # 중간이면 중위 순회 -> 별로 안쓰임
        DFS(v * 2 + 1)
        print(v, end=' ')  # 마지막이면 후위순회 -> 병합정렬은 후위순회


if __name__ == "__main__":
    DFS(1)
