def solution(myString):
    # "x"를 기준으로 문자열을 나누어 배열을 생성합니다.
    parts = myString.split('x')
    
    # 빈 문자열을 제거합니다.
    filtered_parts = [part for part in parts if part]
    
    # 배열을 사전순으로 정렬합니다.
    sorted_parts = sorted(filtered_parts)
    
    return sorted_parts
