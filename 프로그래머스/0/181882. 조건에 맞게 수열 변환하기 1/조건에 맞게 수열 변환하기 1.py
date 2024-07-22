def solution(arr):
    # 새로운 결과 배열 생성
    result = []
    
    # 배열의 각 원소에 대해 조건에 따라 변환
    for num in arr:
        if num >= 50 and num % 2 == 0:
            # 50 이상이고 짝수인 경우 2로 나누기
            result.append(num // 2)
        elif num < 50 and num % 2 == 1:
            # 50 미만이고 홀수인 경우 2를 곱하기
            result.append(num * 2)
        else:
            # 위 조건에 해당하지 않는 경우 원래 값 유지
            result.append(num)
    
    return result