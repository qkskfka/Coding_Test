def solution(arr, flag):
    X = []
    
    for i in range(len(flag)):
        if flag[i]:  # flag[i]가 true인 경우
            X.extend([arr[i]] * (arr[i] * 2))
        else:  # flag[i]가 false인 경우
            X = X[:-arr[i]]
    
    return X
