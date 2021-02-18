def solution(dartResult):
    answer = 0
    
    one=[]
    flag=0
    stage=[]
    ch = 0 #연산 나왔는지
    strs = ['+','+','+']
    dic = {'+':1, '#':-1,'*':'2'}
    #+, *, #
    
    
    for i in dartResult:
        
        if i=='*' or i=='#':
            flag=0
            if len(stage)==1:
                strs[0] = i
            elif len(stage)==2:
                strs[1] = i
            else:
                strs[2]=i
            
        elif i=='S' or i=='D' or i=='T':
            flag=0
            if i=='S':
                stage.append(num)
            elif i=='D':
                stage.append(num**2)
            else:
                stage.append(num**3)
            
        else:
            if flag==1:
                num = 10
                flag = 0
            else:
                num = int(i)
                flag=1
    print(i , '-', num,'-', flag)
      

    # 연산 계싼 
    stage[0] *= int(dic[strs[0]])
    if dic[strs[1]] != 1:
        if strs[1] == '*':
            stage[0] *= 2
            stage[1] *= 2
        else:
            stage[1] *= (-1)
    if strs[2] != '*':
        answer = stage[0] + stage[1] + stage[2]*int(dic[strs[2]])
    else:
        answer = stage[0] + stage[1]*2 + stage[2]*int(dic[strs[2]])

        

    # print(stage,'-', answer,'-',strs)
    return answer

#3번 기회
#0~10점