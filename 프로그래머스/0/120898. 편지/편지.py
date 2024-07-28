def solution(message):
    # 메시지의 길이를 구함
    message_length = len(message)
    
    # 각 문자가 2cm이므로 전체 길이는 메시지 길이에 2를 곱한 값
    needed_length = message_length * 2
    
    return needed_length

