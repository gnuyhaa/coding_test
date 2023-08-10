# 문자열 my_string이 매개변수로 주어집니다. my_string을 거꾸로 뒤집은 문자열을 return하도록 solution 함수를 완성해주세요.

방법1
def solution(my_string):
    my_list = list(my_string)
    my_list.reverse()
    my_str = ''.join(my_list)
    return my_str

방법2
def solution(my_string):
  return my_string[::-1]
