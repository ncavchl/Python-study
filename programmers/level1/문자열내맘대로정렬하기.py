def solution(strings, n):
    return sorted(sorted(strings), key=lambda strings: strings[n])
#인덱스 문자 같은경우를 위해 미리 정렬함