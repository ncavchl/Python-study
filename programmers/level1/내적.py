def solution(a, b):
    answer = 0
    for i in range(0, len(a)):
        answer += int(a[i]) * int(b[i])
    return answer