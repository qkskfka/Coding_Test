def solution(str1, str2):
    result = []
    
    # 두 문자열의 길이
    length = len(str1)
    
    for i in range(length):
        result.append(str1[i])
        result.append(str2[i])
    
    # 리스트를 문자열로 변환
    return ''.join(result)
