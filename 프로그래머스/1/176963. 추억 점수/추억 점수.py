def solution(name, yearning, photo):

    dic = dict(zip(name, yearning))

    a = []
    for p in photo:
        t = list(set(name) & set(p))
        pl = sum([dic[it] for it in t if it in dic])
        a.append(pl)
        
    return a