def solution(priorities, location):
    answer = 0

    array1 = [c for c in range(len(priorities))] # index 위치 저장 
    print(array1)
    array2 = priorities.copy() # 값 저장 (출력되는 값)
    print(array2)
    
    i = 0
    while True:
        if array2[i] < max(array2[i+1:]):
            array1.append(array1.pop(i))
            array2.append(array2.pop(i))
            print(i, ' - ', array1)
        else:
            i += 1

        if array2 == sorted(array2, reverse=True):
            #중요도 역순으로 순서 지정되었을때
            break
    print(array1)
    print(array2)
    return array1.index(location) + 1