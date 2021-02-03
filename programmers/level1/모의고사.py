def solution(answers):
    
    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]
    fc=0
    sc=0
    th=0
    i=0
    for ans in answers:
        if ans == first[i%5]:
            fc +=1
        if ans == second[i%8]:
            sc +=1
        if ans == third[i%10]:
            th +=1
        i+=1
    
    
    MAX = max(fc,sc,th)
    answer = []
    if MAX == fc: answer.append(1)
    if MAX == sc: answer.append(2)
    if MAX == th: answer.append(3)
    return answer