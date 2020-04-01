def solution(L, x):
    """ L = [20, 37, 58, 72, 91] 
        solution(L,5)
        >>>[5, 20, 37, 58, 72, 91]
        """
    for idx in L:
        if x < idx:
            L.insert(L.index(idx),x)
            break
    answer = L
    return answer
    
def solution2(L, x):
    """L = [5, 20, 5, 37, 37, 58, 72, 91]
        soultion2(L,5)
        >>>[0,2]
        """
    answer =[]
    for idx, value in enumerate(L):
        if x == value :
            answer.append(idx)
            continue
    else:
        answer.append(-1)
    return answer
