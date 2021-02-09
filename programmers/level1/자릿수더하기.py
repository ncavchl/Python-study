def solution(n):
    answer = 0

    #1
    num = list(str(n))
    for index in num:
        answer += int(index)
    
    #2
    print(len(str(n)))


    return answer