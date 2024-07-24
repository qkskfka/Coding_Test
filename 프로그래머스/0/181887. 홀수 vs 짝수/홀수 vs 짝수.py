def solution(num_list):
    odd_sum = sum(num_list[i] for i in range(0, len(num_list), 2))  # 홀수 번째 원소들의 합 (1번, 3번, 5번, ...)
    even_sum = sum(num_list[i] for i in range(1, len(num_list), 2))  # 짝수 번째 원소들의 합 (2번, 4번, 6번, ...)
    
    return max(odd_sum, even_sum)

# 예시 입력 테스트
print(solution([4, 2, 6, 1, 7, 6]))  # 17
print(solution([-1, 2, 5, 6, 3]))    # 8
