def solution(n, lost, reserve): 
    reser = set(reserve)-set(lost) 
    lost = set(lost)-set(reserve)
    #print(reser , "-", lost)
    for i in reser: 
        if i-1 in lost: 
            lost.remove(i-1) 
        elif i+1 in lost: 
            lost.remove(i+1) 
    return n-len(lost)