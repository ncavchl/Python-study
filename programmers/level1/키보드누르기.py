def solution(numbers, hand):
    answer = ''
    mapx = [1,0,1,2,0,1,2,0,1,2,0,2]
    mapy = [3,0,0,0,1,1,1,2,2,2,3,3]
    #3번이면 mapx[3] = 2, mapy[3] = 0
    left = 10
    right = 11
    for num in numbers:
        if num==1 or num==4 or num==7 :
            left = num
            answer += 'L'
        elif num==3 or num==6 or num==9:
            right = num
            answer += 'R'
        else:
            
            le = abs(mapx[num] - mapx[left]) + abs(mapy[num]-mapy[left])
            ri = abs(mapx[num] - mapx[right]) + abs(mapy[num]-mapy[right])
            # print(le, '-', ri ,' -', num)
            if le>ri:
                right = num
                answer += 'R'
            elif le<ri:
                left = num
                answer += 'L'
            else:
                if hand=='right':
                    right = num
                    answer += 'R'
                else:
                    left = num
                    answer += 'L'
                
        # print('left:', left, '+right:', right)
    left = 0
    right = 11
    return answer