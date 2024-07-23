def solution(my_string):
    # 접미사를 저장할 리스트
    answer = []
    
    # 모든 접미사 추출
    for i in range(len(my_string)):
        suffix = my_string[i:]
        answer.append(suffix)
    
    # 접미사를 사전순으로 정렬
    answer.sort()
    
    return answer
