def solution(board, moves):
    answer = 0
    bucket = []
    for m in moves:
        check=0
        for index in range(len(board)):
            if board[index][m-1] != 0 and check==0:
                num = board[index][m-1]
                bucket.append(num)
                board[index][m-1] = 0
                check=1
                continue
        # print(bucket)  
        if len(bucket) > 1:
            if bucket[-1] == bucket[-2]:
                answer += 2
                del bucket[-2]
                del bucket[-1]
                print(answer, m)
                
    
    # print(bucket)            
    
#     for i in range(5):
#         map.append([])
#         for j in range(5):
#             num = board[j][i] 
#             if num !=0:
#                 map[i].append(num)
            
#     arr = []
#     for index, k in enumerate(moves):
#         if index==0:
#             arr.append(map[k-1][0])
#             del map[k-1][0]
#         else: 
#             if arr[-1] == k:
#                 answer += 2
#                 del arr[-1]
#             else:
#                 arr.append(map[k-1][0])
#                 del map[k-1][0]
            

    return answer