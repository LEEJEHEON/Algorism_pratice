def solution(progresses, speeds):
    answer = []
    i = 0
    while i != len(progresses):
        count = 0
        progresses = [progresses + speeds for progresses,speeds in zip(progresses,speeds)]
        for j in range(i,len(progresses)):
            if progresses[j] >= 100:
                count += 1
                i +=1
            else:
                break
                
        if count != 0:
            answer.append(count) 
        
    return answer