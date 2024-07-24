def solution(myString, pat):
    # 패턴의 길이
    pat_len = len(pat)
    
    # 문자열의 길이
    str_len = len(myString)
    
    # 가장 긴 부분 문자열을 저장할 변수
    longest_substr = ""
    
    # 문자열의 끝에서부터 탐색
    for i in range(str_len - pat_len + 1):
        # 현재 인덱스에서 pat이 myString의 부분 문자열로 끝나는지 확인
        if myString[i:i + pat_len] == pat:
            # 현재 인덱스까지의 부분 문자열을 저장
            current_substr = myString[:i + pat_len]
            # 가장 긴 부분 문자열을 업데이트
            if len(current_substr) > len(longest_substr):
                longest_substr = current_substr
                
    return longest_substr
