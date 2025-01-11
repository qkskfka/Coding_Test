def solution(myString):
    # 문자열을 'x'를 기준으로 나눕니다.
    parts = myString.split('x')
    
    # 각 부분 문자열의 길이를 리스트에 저장합니다.
    lengths = [len(part) for part in parts]
    
    return lengths