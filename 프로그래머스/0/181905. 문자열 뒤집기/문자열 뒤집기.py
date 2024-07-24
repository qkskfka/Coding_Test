def solution(my_string, s, e):
    # 1. 부분 문자열 추출
    substring = my_string[s:e+1]
    
    # 2. 부분 문자열 뒤집기
    reversed_substring = substring[::-1]
    
    # 3. 문자열 합치기
    result = my_string[:s] + reversed_substring + my_string[e+1:]
    
    return result
