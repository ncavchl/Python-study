def solution(x):
    arr = list(str(x))
    sum = 0
    for i in arr:
        sum += int(i)
    
    if x % sum == 0:
        return True
    else:
        return False