def solution(my_string, indices):
    # 문자열을 리스트로 변환하여 mutable하게 만듭니다.
    my_string_list = list(my_string)
    
    # 인덱스 리스트를 정렬한 후 역순으로 접근하여 원소를 제거합니다.
    for index in sorted(indices, reverse=True):
        del my_string_list[index]
    
    # 리스트를 문자열로 변환하여 반환합니다.
    return ''.join(my_string_list)
