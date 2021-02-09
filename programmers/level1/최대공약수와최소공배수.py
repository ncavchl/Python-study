# from math import gcd
def solution(n, m):
    # ml = gcd(n,m)
    ml = n
    mr = n*m
    
    min2 = min(n,m)
    max2 = max(n,m)
    if(max2%min2 == 0): ml = min2
    else:
        while min2!=0:
            temp = max2
            max2 = min2
            min2 = temp % min2
        ml = max2
    

    mr = mr / ml
    answer = [ml, mr]
    return answer