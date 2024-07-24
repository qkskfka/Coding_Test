def solution(arr):
    # 배열의 길이
    n = len(arr)
    
    # 배열의 길이가 2의 거듭제곱인지 확인
    # 2의 거듭제곱인지 확인하는 방법: 길이 & (길이 - 1) == 0
    if (n & (n - 1)) == 0:
        return arr
    
    # 배열의 길이를 2의 거듭제곱으로 만드는 데 필요한 0의 개수
    # 2의 거듭제곱 중에서 가장 가까운 값 계산
    power_of_two = 1
    while power_of_two < n:
        power_of_two *= 2
    
    # 추가해야 할 0의 개수
    num_zeros_to_add = power_of_two - n
    
    # 0을 추가한 배열 생성
    return arr + [0] * num_zeros_to_add
