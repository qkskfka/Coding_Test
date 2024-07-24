def solution(num_list):
    def count_operations(num):
        count = 0
        while num > 1:
            if num % 2 == 0:  # 짝수인 경우
                num //= 2
            else:  # 홀수인 경우
                num = (num - 1) // 2
            count += 1
        return count

    total_operations = sum(count_operations(num) for num in num_list)
    return total_operations
