def solution(n, k):
    answer = 0
    val = changeValue(n, k)
    tmp = []
    s = ''
    for i in val:
        if i == '0' and s != '':
            tmp.append(int(s))
            s = ''
            continue
        else:
            s += i

    if s != '':
        tmp.append(int(s))

    for i in tmp:
        if isPrime(i):
            answer += 1

    return answer

def isPrime(k):
    if k==2 or k==3: return True
    if k%2==0 or k<2: return False
    for i in range(3, int(k**0.5)+1, 2):
        if k%i==0:
            return False

    return True

def changeValue(n, k):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, k)
        rev_base += str(mod)

    return rev_base[::-1]
    # 역순인 진수를 뒤집어 줘야 원래 변환 하고자하는 base가 출력


n = 110011
k = 10

print(solution(n, k))
#12분 54초
