def solution(skill, skill_trees):
    answer = 0
    
    
    for i in skill_trees:
        lens = len(i)
        check = -1
        checkp = 1
        for v in range(0,lens):
            # print(i[v], '-', check, '-',v)
            if i[v] in skill:
                if skill[check+1] == i[v]:
                    check += 1
                else:
                    # print('불가능')
                    checkp = 0
            if checkp == 0:
                break
        if checkp == 1:
            answer += 1
            
        
    return answer