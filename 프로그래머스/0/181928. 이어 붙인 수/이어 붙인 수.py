def solution(num_list):
    answer = 0
    a = "" #홀
    b = "" #짝
    
    for i in num_list:
        if i%2 != 0:
            a += str(i)
        else:
            b += str(i)
    return int(a) + int(b)