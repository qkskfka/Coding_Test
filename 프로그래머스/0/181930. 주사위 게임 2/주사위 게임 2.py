def solution(a, b, c):
    if a == b == c:
        sum_a = a + b + c
        sum_b = a**2 + b**2 + c**2
        sum_c = a**3 + b**3 + c**3
        return sum_a * sum_b * sum_c
    
    elif a == b or a == c or b == c:
        sum_a = a + b + c
        sum_b = a**2 + b**2 + c**2
        return sum_a * sum_b
    else:
        return a + b + c