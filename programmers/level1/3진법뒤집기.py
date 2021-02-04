def solution(n):
    three = ''
    while n!=0:
        three += str(n%3)
        n = n//3
    print(three)     
    answer = 0
    for index, t in enumerate(three[::-1]):
        print(index,"=",t)
        answer += ((3**index) * int(t))
        
    return answer