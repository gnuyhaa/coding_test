def solution(my_string):
    result = ''.join(dict.fromkeys(my_string))
    
    return result
