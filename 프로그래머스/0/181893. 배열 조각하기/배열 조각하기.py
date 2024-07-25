def solution(arr, query):
    for i in range(len(query)):
        if i % 2 == 0:
            arr = arr[:query[i] + 1]  # 짝수 인덱스에서 query[i] 번 인덱스 뒷부분 잘라내기
        else:
            arr = arr[query[i]:]  # 홀수 인덱스에서 query[i] 번 인덱스 앞부분 잘라내기
    return arr

# 입출력 예시
arr = [0, 1, 2, 3, 4, 5]
query = [4, 1, 2]
result = solution(arr, query)
print(result)  # 출력: [1, 2, 3]
