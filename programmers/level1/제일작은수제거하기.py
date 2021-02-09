import copy
def solution(arr):
    if len(arr) == 1:
        return [-1]
    else:
        ori = copy.deepcopy(arr)
        arr.sort()
        ori.remove(arr[0])

        return ori
        
    # answer = []
    # return answer