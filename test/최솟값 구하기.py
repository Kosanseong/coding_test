arr = [5, 3, 7, 9, 2, 5, 2, 6]
arrMin = float('inf')  # 파이썬의 가장 큰 값
index = 0
for i in range(len(arr)):
    '''
     문제중에 앞에 것을 구하면 <으로 뒤에 것을 넣으라고 하면
     <=으로 뒤에 값으로 변경 시켜줘야 한다.
    '''
    if arr[i] <= arrMin:
        arrMin, index = arr[i], i
print(arrMin, index)

