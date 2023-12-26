def solution(spell, dic):
    for word in dic : 
        if len(spell) == len([1 for s in spell if s in word]) :
            return 1
    return 2
