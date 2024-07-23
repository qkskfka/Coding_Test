def solution(my_string, is_suffix):
    # my_string이 is_suffix로 끝나는지 확인
    if my_string.endswith(is_suffix):
        return 1
    else:
        return 0