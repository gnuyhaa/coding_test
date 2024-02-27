def solution(a, b):
    days = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    day = 1
    cal = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    for i in range(1, a):
        day += cal[i]
    day += b-1
    answer = days[day%7]
    return answer
