def solution(x):
    X = list(map(int, str(x)))
    Sum = sum(X)
    
    if x % Sum == 0 :
        return True
    else :
        return False
