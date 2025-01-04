def solution(num_list):
    # 마지막 원소와 그 전 원소를 가져옵니다.
    last_element = num_list[-1]
    second_last_element = num_list[-2]
    
    # 조건에 따라 새로운 값을 계산합니다.
    if last_element > second_last_element:
        new_value = last_element - second_last_element
    else:
        new_value = last_element * 2
    
    # 새로운 값을 리스트에 추가합니다.
    num_list.append(new_value)
    
    return num_list
