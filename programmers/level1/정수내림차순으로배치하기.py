def solution(n):
    
    num = list(str(n))
    num.sort(reverse = True)
    # answer = map(int, num)
    answer = int(''.join(num))
    
    return answer