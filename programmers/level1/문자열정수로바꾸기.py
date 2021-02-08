def solution(s):
    num = 0
    if s[0] == "-":
        num = int(s[1:]) * -1
    else:
        num = int(s)
    answer = num
    return answer