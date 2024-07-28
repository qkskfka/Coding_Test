def solution(n):
    # n x n 배열 초기화
    matrix = [[0] * n for _ in range(n)]
    
    # 방향 벡터 설정 (오른쪽, 아래, 왼쪽, 위)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    current_direction = 0
    
    # 초기 위치 설정
    row, col = 0, 0
    
    for num in range(1, n * n + 1):
        matrix[row][col] = num
        
        # 다음 위치 계산
        next_row = row + directions[current_direction][0]
        next_col = col + directions[current_direction][1]
        
        # 다음 위치가 배열의 범위를 벗어나거나 이미 값이 채워져 있는 경우 방향 전환
        if next_row < 0 or next_row >= n or next_col < 0 or next_col >= n or matrix[next_row][next_col] != 0:
            current_direction = (current_direction + 1) % 4
            next_row = row + directions[current_direction][0]
            next_col = col + directions[current_direction][1]
        
        # 현재 위치 갱신
        row, col = next_row, next_col
    
    return matrix
