def getUbak(k):
    result = []
    while k != 1:
        result.append(k)
        # 결과가 소수이므로 / 연산
        k = k / 2 if k % 2 == 0 else k * 3 + 1 
    result.append(k)
    return result
 
def solution(k, ranges):
    answer = []
    ubak = getUbak(k)
 
    for r in ranges:
        total = 0
        ubakRange = ubak[r[0] : len(ubak)+r[1]]
        
        # 주어진 구간의 시작점이 끝점보다 커서 유효하지 않은 구간
        if r[0] >= r[1] + len(ubak):
            answer.append(-1)
            continue
            
        for i in range(len(ubakRange) - 1):
            # 사다리꼴 넓이 구하는 공식 : ((윗변+아랫변) * 높이) / 2
            total += (((ubakRange[i] + ubakRange[i+1]) * 1) / 2)
        answer.append(total)
        
    return answer
