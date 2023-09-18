# 이 때 "Z"가 나오면 바로 전에 더했던 숫자를 뺀다는 뜻입니다. 숫자와 "Z"로 이루어진 문자열 s가 주어질 때, 머쓱이가 구한 값을 return 하도록 solution 함수를 완성해보세요.

def solution(s):
    stack = []
    for n in s.split(' '):
        try: # n이 숫자일 경우
            stack.append(int(n))
        except: # n이 숫자가 아닐경우 
            stack.pop()
    return sum(stack)
