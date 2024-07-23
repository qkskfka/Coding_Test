def solution(my_string, m, c):
    # m 길이의 줄로 나누어 각 줄을 저장합니다.
    rows = [my_string[i:i + m] for i in range(0, len(my_string), m)]
    
    # c-1 번째 열의 문자를 각 줄에서 추출합니다.
    result = ''.join(row[c - 1] for row in rows)
    
    return result
