def solution(arr, divisor):
    answer = []
    for a in arr :
        if a % divisor == 0 :
            answer.append(a)
    answer.sort()
    
    if len(answer) == 0 :
        return [-1]
    
    return answer

