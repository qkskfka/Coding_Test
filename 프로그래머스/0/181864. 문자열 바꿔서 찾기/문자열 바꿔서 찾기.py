def solution(myString, pat):
    answer=''
    for i in myString:
        if i=='A':
            answer+='B'
        elif i=='B':
            answer+='A'
        else:
            answer+=i

    return int(pat in answer)