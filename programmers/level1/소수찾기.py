def solution(n):
    num = set(range(2, n+1))
    # print(list(range(2*2, 10+1, 2)))
              
    for i in range(2, n+1):
        if i in num:
                num -= set(range(2*i, n+1, i))

    answer = len(num)
    return answer