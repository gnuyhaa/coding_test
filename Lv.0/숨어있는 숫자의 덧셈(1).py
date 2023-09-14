# 문자열 my_string이 매개변수로 주어집니다. my_string안의 모든 자연수들의 합을 return하도록 solution 함수를 완성해주세요.

# 다른사람 풀이 
import re 
def solution(my_string):
    return sum(int(i) for i in str(re.sub(r'[^0-9]', '', my_string)))
