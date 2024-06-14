import itertools

def solution(k, dungeons):
    permutation_list = list(itertools.permutations(dungeons))
    
    answer = []   # 모든 경우의 수에 대한 탐험 가능한 던전 개수 모음
    for p in permutation_list: 	
        total = 0   # 탐험 가능 던전 수
        k_copy = k  # k가 바뀐 채로 다음 경우의 수를 탐색하는 것을 방지
        for i, j in p:   # i: 최소 필요 피로도, j: 소모 피로도
        	# print(f'k:{k_copy}, i:{i}, j:{j}')
            if i > k_copy:
                break
            else:
                k_copy = k_copy-j
                total += 1   # 탐험 가능 던전 수 1증가
                
        answer.append(total)

    return max(answer)
