def solution(arr, intervals):
    # 첫 번째 구간 추출
    a1, b1 = intervals[0]
    first_part = arr[a1:b1+1]
    
    # 두 번째 구간 추출
    a2, b2 = intervals[1]
    second_part = arr[a2:b2+1]
    
    # 두 구간을 결합하여 새로운 배열 생성
    result = first_part + second_part
    
    return result

# 예시 테스트
arr = [1, 2, 3, 4, 5]
intervals = [[1, 3], [0, 4]]
print(solution(arr, intervals))  # 출력: [2, 3, 4, 1, 2, 3, 4, 5]
