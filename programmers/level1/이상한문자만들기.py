import string
def solution(s):
    answer = ''
    index = 0
    for i in s:
        if i.isalpha():
            index += 1
            if index % 2 != 0:
                answer += i.upper()
            else :
                answer += i.lower()
        else:
            answer+= ' '
            index = 0
            continue

        print(index, "-", answer)

    return answer