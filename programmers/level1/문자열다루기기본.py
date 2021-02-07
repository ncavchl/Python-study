def solution(s):
    ss = s
    s = list(s)
    
    answer = True
    if len(s) == 4 or len(s) == 6:
        if ss.isdigit():
            return True
    return False