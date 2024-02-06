def solution(s):
    if len(s) == 4 or len(s) == 6:
        answer = True
    else:
        return False
    return s.isdigit()


# 간략한 코드
def solution(s):
    return s.isdigit() and len(s) in [4, 6]
