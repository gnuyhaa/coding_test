def solution(N, stages): # 실패율 O(n**2)
    answer = []
    fail_list=[]
    dic_list={}
    answer_list=[]
    for i in range(1, N+1):
        full=0
        reach=0
        for j in stages:
            if j >= i:
                full+=1
            if j == i:
                reach+=1
        if full==0:
            dic_list[i]=0
        else:            
            dic_list[i]=reach/full 

    # return dic_list
    
    dict1=sorted(dic_list, key=lambda x : x[1], reverse=True)
    
    for i in dict1:
        answer.append(i[0])

    return answer
