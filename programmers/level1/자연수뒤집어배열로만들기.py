def solution(n):
    answer = []
    num = list(str(n))
    for i in range(0, len(num)):
        answer.append(int(num[len(num)-1-i]))
    
    return answer