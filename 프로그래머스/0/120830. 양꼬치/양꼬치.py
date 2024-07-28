def solution(n, k):
    # 양꼬치 가격 계산
    yang_price = n * 12000
    
    # 서비스 음료수 개수 계산
    free_drinks = n // 10
    
    # 음료수 가격 계산 (서비스 음료수를 제외한)
    drink_price = (k - free_drinks) * 2000
    
    # 총 가격 계산
    total_price = yang_price + drink_price
    
    return total_price
