def solution(w,h):
    answer = 1
    
    max1 = max(w,h)
    min1 = min(w,h)
    if(max1%min1 == 0): ml=min1
    else:
        while min1 != 0:
            temp = max1
            max1 = min1
            min1 = temp%min1
        ml = max1
    print(ml)
    
    answer = w*h - (w+h-ml)
        
    return answer