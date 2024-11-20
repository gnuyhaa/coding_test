T = int(input())
nums = [2, 3, 5, 7, 11]
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    temp = {2: 0, 3: 0, 5: 0, 7: 0, 11: 0} # [2^a, 3^b, 5^c, 7^d, 11^e] 카운트
    N = int(input())
    for i in nums:
        while True:
            if N % i == 0: # 0으로 나누어 떨어진다면, 
                N = N // i # 나눈다.
                temp[i] += 1
            else:
                break

    print("#{0} {1} {2} {3} {4} {5}".format(test_case, list(temp.values())[0],
                                            list(temp.values())[1], list(temp.values())[2],
                                            list(temp.values())[3], list(temp.values())[4],))
