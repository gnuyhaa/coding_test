def solution(num, k):
    answer = 0
    n=str(num)
    
    for i in n:
        answer += 1
        if i == str(k):
            return answer
    return -1
    return answer
