def solution(n):
    answer = ''
    while n>0:
        rest = n % 3
        n = n // 3
        answer += str(rest)
        
    return int(answer,3)