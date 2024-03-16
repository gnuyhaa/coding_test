1. 십진수 입력을 이진수로 변환하기
2. 지도1과 지도2의 암호화된 배열 비교하기
3. 비교 후 공백과 '#'으로 표현한 code를 차례차례 answer 리스트에 넣어주기

def solution(n, arr1, arr2):
    answer = []
    bin1 = []
    bin2 = []
    
    # 이진수로 변환하기
    for dec in arr1:
        bin1.append(bin(dec)[2:].zfill(n))
    
    for dec in arr2:
        bin2.append(bin(dec)[2:].zfill(n))
        
    code = ""
    
    for i in range(len(bin1)):
        
        for j in range(len(bin1[i])):
            if bin1[i][j] == "0" and bin2[i][j] == "0":
                code += " "
            elif bin1[i][j] == "1" and bin2[i][j] == "1":
                code += "#"
            else:
                code += "#"
            
        answer.append(code)
        code = ""
    
    return answer
