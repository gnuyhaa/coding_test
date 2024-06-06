def solution(picks, minerals):
    answer = 0
    
    score = {0:{"diamond":1,"iron":1,"stone":1},
             1:{"diamond":5,"iron":1,"stone":1},
             2:{"diamond":25,"iron":5,"stone":1}}
    
    minerals = [minerals[i:i+5] for i in range(0,len(minerals),5)][:sum(picks)]
    
    minerals.sort(key=lambda x : (x.count("diamond"),x.count("iron"),x.count("stone")),reverse=True)
    for m in minerals:
        if picks[0] > 0:
            picks[0] -= 1
            for i in m:
                answer += score[0][i]
        elif  picks[1] > 0:
            picks[1] -= 1
            for i in m:
                answer += score[1][i]
        else:
            picks[2] -= 1
            for i in m:
                answer += score[2][i]
            
    return answer
