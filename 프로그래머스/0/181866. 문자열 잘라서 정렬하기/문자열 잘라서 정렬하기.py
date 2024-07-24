def solution(myString):
    # "x"를 기준으로 문자열을 분리합니다.
    parts = myString.split('x')
    
    # 빈 문자열을 제거합니다.
    non_empty_parts = [part for part in parts if part]
    
    # 결과를 사전순으로 정렬합니다.
    sorted_parts = sorted(non_empty_parts)
    
    return sorted_parts

