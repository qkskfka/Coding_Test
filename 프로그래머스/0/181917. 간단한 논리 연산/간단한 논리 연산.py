def solution(x1, x2, x3, x4):
    # Calculate (x1 ∨ x2)
    or_result1 = x1 or x2
    
    # Calculate (x3 ∨ x4)
    or_result2 = x3 or x4
    
    # Calculate (x1 ∨ x2) ∧ (x3 ∨ x4)
    final_result = or_result1 and or_result2
    
    return final_result
