def solution(begin, target, words):
    if target not in words:  #타깃이 애초에 없을 경우 변환이 안되므로 0 리턴.
        return 0

    N=len(words)+1
    floyd=[[51]*N for _ in range(N)]  #begin에서 해당 단어로 바꿀 수 있는 최대값은 50이다.

    words.insert(0,begin)

    for i in range(N):
        for j in range(N):
            if i==j or words[i]==words[j]:
                floyd[i][j]=0
            else:
                cnt=0
                for idx,ch in enumerate(words[i]):
                    if ch!=words[j][idx]:
                        cnt+=1
                if cnt==1:
                    floyd[i][j]=1

    for transit in range(N):
        for start in range(N):
            for destination in range(N):
                floyd[start][destination]=min(floyd[start][transit]+floyd[transit][destination],floyd[start][destination])

    #타깃까지의 최소 변환 횟수가 51보다 작아야 해당 값을 리턴.
    if floyd[0][words.index(target)]<51:
        return floyd[0][words.index(target)]
    else:  #아니면 변환이 안되는 경우이므로 0 리턴.
        return 0
