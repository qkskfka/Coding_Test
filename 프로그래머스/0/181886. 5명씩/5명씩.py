def solution(names):
    # 결과를 저장할 리스트
    result = []
    
    # 5명씩 그룹을 나누기 위한 루프
    for i in range(0, len(names), 5):
        # 각 그룹의 첫 번째 사람의 이름을 result에 추가
        result.append(names[i])
    
    return result