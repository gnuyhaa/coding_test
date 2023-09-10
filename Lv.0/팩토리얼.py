# 5! = 5 * 4 * 3 * 2 * 1 = 120

# n	result
# 3628800	10
# 7	3

from math import factorial

def solution(n):
    answer = 10
    while n < factorial(answer):
        answer -= 1
    return answer
