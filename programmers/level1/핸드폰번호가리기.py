def solution(phone_number):
    arr = list(str(phone_number))
    for i in range(0, len(phone_number)-4):
        arr[i] = '*'
    answer = ''.join(arr)
    print(answer)
    return answer