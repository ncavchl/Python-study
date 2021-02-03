from itertools import combinations
def solution(numbers):
    answer = set()
    #set으로 같은 요소가 존재하는 경우 배제 가능
    for i in list(combinations(numbers,2)):
        answer.add(sum(i))
        
    answer = sorted(answer)
    
    return answer


# from itertools import combinations
# def solution(numbers):
#     answer = set()
#     for i in list(combinations(numbers,2)):
#         answer.add(sum(i))
#     return sorted(answer)