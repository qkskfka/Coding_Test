def solution(arr, queries):
    # 각 쿼리에 대해 배열을 업데이트
    for s, e in queries:
        for i in range(s, e + 1):
            arr[i] += 1
    return arr
