def solution(number):
    # 각 자리 숫자의 합을 계산합니다.
    digit_sum = sum(int(digit) for digit in number)
    
    # 그 합을 9로 나눈 나머지를 반환합니다.
    return digit_sum % 9

