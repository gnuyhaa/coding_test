def solution(common):
    if common[1] - common[0] == common[2] - common[1]:
        # 등차
        answer = common[-1]+(common[1]-common[0])
    elif common[1] / common[0] == common[2] / common[1]:
        # 등비
        answer = common[-1]*(common[1]/common[0])
    return answer
