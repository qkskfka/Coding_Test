def solution(intStrs, k, s, l):
    result = []
    
    for string in intStrs:
        # 부분 문자열 추출
        substring = string[s:s+l]
        
        # 정수로 변환
        number = int(substring)
        
        # 정수 값이 k보다 큰지 확인
        if number > k:
            result.append(number)
    
    return result
