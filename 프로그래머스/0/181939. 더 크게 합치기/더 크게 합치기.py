def solution(a, b):

    aa = int(str(a) + str(b))
    bb = int(str(b) + str(a))
    
    if aa > bb:
        return  aa
    elif aa < bb:
        return  bb
    else :
        return  aa
    