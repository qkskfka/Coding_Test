def solution(board, k):
    total_sum = 0
    
    # board의 행과 열을 순회하면서 조건을 확인합니다.
    for i in range(len(board)):
        for j in range(len(board[i])):
            if i + j <= k:
                total_sum += board[i][j]
    
    return total_sum
