def solution(myString):
    res =""
    for i in myString:
        if i == "a":
            res += "A"
        elif i=="A":
            res += "A"
        else:
            res += i.lower()
    return res
