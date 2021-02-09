def solution(n):
    num = pow(n, 0.5)
    if num%1 != 0:
        return -1
    else:
        return (num+1)**2
    # print(num)
    # answer = 0
    # return answer