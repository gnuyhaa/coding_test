# 장군개미 공격력 5, 병정개미 공격력 3, 일개미 공격력 1
# 사냥감의 체력 hp가 매개변수로 주어질 때, 사냥감의 체력에 딱 맞게 최소한의 병력을 구성하려면 몇 마리의 개미가 필요한지를 return하도록 solution 함수를 완성해주세요.

def solution(hp):
    general = hp //5
    solider = (hp-(5*general))//3
    normal = (hp-(5*general)-(3*solider))//1
    
    return general + solider + normal
