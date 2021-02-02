def solution(participant, completion):
    participant.sort()
    completion.sort()
   # print('hi')
    for p,c in zip(participant, completion):
        #print(p, "-", c)
        if p != c:          #동명이인 탐색 
            return p
    return participant.pop()