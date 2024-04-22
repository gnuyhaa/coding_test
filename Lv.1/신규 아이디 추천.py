def solution(new_id):
    # 규칙에 맞게 ID 추천하기
    
    # (1) 대문자 -> 소문자로 변환
    new_id = new_id.lower()
    
    # (2) 소문자, 숫자, "-", "_", "." 외 단어 제거
    dic = ["-", "_", "."]
    check = []
    for i in range(len(new_id)):
        if new_id[i] not in dic:
            if new_id[i].isalpha() or new_id[i].isdigit():
                continue
            else:
                check.append(new_id[i]) # dic에 없는 특수문자를 따로 저장
    for j in range(len(check)):
        new_id = new_id.replace(check[j], "") # 특수문자 제거
        
    # (3) "." 두 번 이상 등장 -> "." 하나로 치환
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
        
    # (4) "."이 처음 or 끝에 있다면? -> 제거
    if len(new_id) > 0:
        if new_id[0] == '.':
            new_id = new_id[1:]
        
    if len(new_id) > 0:
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    
    # (5) 빈 문자열이면 a 대입
    if len(new_id) == 0:
        new_id = 'a'
        
    # (6) id의 길이가 16 이상이면 0:15까지만 남기고 제거
    if len(new_id) > 15:
        new_id = new_id[0:15] # 0번 ~ 14번
        if new_id[-1] == ".": # 만약 마지막 글자가 . 이면 제거
            new_id = new_id[:-1]
    
    # (7) id의 길이가 2자 이하라면 new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 붙임.
    if len(new_id) <= 2:
        while True:
            if len(new_id) == 3:
                break
            else:
                last_a = new_id[-1]
                new_id = new_id + last_a
                
    answer = new_id
    return answer
