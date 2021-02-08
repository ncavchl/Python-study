import string
def solution(s, n):
    answer = ""
    base = ""
    for c in s:
        if c in string.ascii_lowercase:
            base = string.ascii_lowercase
        elif c in string.ascii_uppercase:
            base = string.ascii_uppercase
        else:
            answer += c
            continue
        index = base.index(c) + n
        answer += base[index % len(base)]
    return answer