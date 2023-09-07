# 약수의 개수가 세 개 이상인 수를 합성수
# 자연수 n이 매개변수/ n 이하의 합성수의 개수 return

def solution(n):
    answer = 0
    
    for i in range(n+1):
        c = 0 # 약수의 개수를 찾기 위한 변수
        for j in range(1, i+1):
            if i % j == 0:
                c += 1
        if c >= 3:
            answer += 1
    return answer
