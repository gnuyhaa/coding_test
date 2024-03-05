def solution(n, m):
    answer = []
    arr1 = []
    for i in range(1, min(n, m)+1):
        if n%i == 0 and m%i ==0: # 동시에 나눠지면 공약수
            arr1.append(i)
    for i in range(max(n, m), (n*m)+1):
        if i%n == 0 and i%m == 0:
            min_num = i
            break
    max_num = max(arr1)
    answer.append(max_num)
    answer.append(min_num)
    return answer


# 유클리드 호제법
def gcd(n, m):
    if n%m == 0:
        return m
    else:
        return gcd(m, n%m)
    
def solution(n, m):
    answer = [gcd(m, n), n*m // gcd(m,n)]
    return answer
