def solution(n):
    # n x n 크기의 이차원 배열을 생성하고 모든 값을 0으로 초기화
    arr = [[0] * n for _ in range(n)]
    
    # 주 대각선 원소를 1로 설정
    for i in range(n):
        arr[i][i] = 1
        
    return arr
