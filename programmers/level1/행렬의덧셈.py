def solution(arr1, arr2):
    answer = []
    len1 = len(arr1[0])
    print(len1)
    for i in range(0,len(arr1)):
        ans = []
        for j in range(0,len1):
            ans.append(arr1[i][j] + arr2[i][j])
        answer.append(ans)
    
    return answer