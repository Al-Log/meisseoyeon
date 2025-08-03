def solution(s):
    answer = []
    cindex = {}
    for i, char in enumerate(s):
        if char in cindex:
            answer.append(i - cindex[char])
        else:
            answer.append(-1)
        cindex[char] = i
    return answer          