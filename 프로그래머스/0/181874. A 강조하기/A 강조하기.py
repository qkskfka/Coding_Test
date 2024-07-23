def solution(myString):
    result = []
    
    for char in myString:
        if char == 'a':
            result.append('A')
        elif char.isupper() and char != 'A':
            result.append(char.lower())
        else:
            result.append(char)
    
    return ''.join(result)
