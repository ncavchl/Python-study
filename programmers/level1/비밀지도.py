def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        #이진법 변환 
        arr1[i] = int(format(arr1[i],'b'))
        arr2[i] = int(format(arr2[i],'b'))
        
        k=''
        a = str(arr1[i] + arr2[i])
        print(a)
        if len(a) < n:
            #자리가 더했는데도 짧으면 앞에 0 채우기 
            a='0'*(n-len(a)) + a
            
        for j in a:
            if j == '0' :
                k = k + ' '
            else:
                k += '#'
        answer.append(k)
    return answer