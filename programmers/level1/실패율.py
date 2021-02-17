def solution(N, stages):
    result = {}
    num = len(stages)
    
    #딕셔너리 개념 사용
    for stage in range(1, N+1):
        if num != 0:
            count = stages.count(stage)
            result[stage] = count / num
            num -= count
        else:
            result[stage] = 0
    # print(result)
    #키는 실패율 높은 순  - 실패율 오름차순의 역순으로 옵션

    #오른쪽 값 기준으로 정렬해서 왼쪽값으로 출력
    answer = sorted(result, key=lambda x : result[x], reverse=True)
    # print(answer)
    return answer