def solution(s):
    answer = False
    p = 0
    y = 0
    for ch in s:
        #print(ch)
        if ch == 'p' or ch == 'P':
            p += 1
        if ch == 'y' or ch=='Y':
            y += 1
    print(p, '-', y)
    if p == y:
        answer = True

    return answer