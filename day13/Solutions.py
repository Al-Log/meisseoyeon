def solution(x):
    sum=0
    arr= list(str(x))
    for i in range (len(arr)):
        sum+=int(arr[i])
        if x%sum==0: 
            answer= True
        else:
            answer= False
    return answer