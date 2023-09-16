# 예를 들어 12를 소인수 분해하면 2 * 2 * 3 으로 나타낼 수 있습니다. 따라서 12의 소인수는 2와 3입니다.

def solution(n):
    answer = []
    
    x = 2
    while x <= n:
        if n % x == 0:
            if x not in answer:
                answer.append(x)
            n //= x
        else:
            x += 1
    return answer
