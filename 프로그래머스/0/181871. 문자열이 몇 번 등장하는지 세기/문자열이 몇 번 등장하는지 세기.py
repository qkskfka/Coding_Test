def solution(myString, pat):
    count = 0
    start = 0
    
    while True:
        start = myString.find(pat, start)
        if start == -1:
            break
        count += 1
        start += 1  # Move to the next character for overlapping occurrences
    
    return count
