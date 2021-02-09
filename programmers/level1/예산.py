def solution(d, budget):
    d.sort()
    sum = 0
    answer = 0
    index=0
    # while index<len(d)+1 and answer<budget+1:
    #     answer += d[index]
    #     index += 1
    print(d)
    for i in range(0, len(d)):
        if sum+d[i] < budget+1:
            sum += d[i]
            answer = i+1
        print(sum, '-', answer)
    
    return answer