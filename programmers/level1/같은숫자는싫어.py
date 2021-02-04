def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in range(len(arr)-1):
        i = i+1
        if arr[i] != arr[i-1]:
            answer.append(arr[i])

    return answer