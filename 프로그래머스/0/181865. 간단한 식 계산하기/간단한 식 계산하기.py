def solution(binomial):
    # 문자열을 공백을 기준으로 분리
    parts = binomial.split()
    
    # 분리된 요소들 추출
    a = int(parts[0])
    op = parts[1]
    b = int(parts[2])
    
    # 연산자에 따라 계산 수행
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        raise ValueError("지원되지 않는 연산자입니다.")
