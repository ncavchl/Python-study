def solution(n):
    answer = ''
    i1 = n//2
    i2 = n%2
    for index in range(0,i1):
        answer += "수박"
    if i2 == 1:
        answer += "수"
        
        
    return answer