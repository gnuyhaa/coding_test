def solution(arr):
    answer = 0
    cnt = 0
    for i in arr:
        answer += i
        cnt += 1
    avg = answer / cnt
    return avg
