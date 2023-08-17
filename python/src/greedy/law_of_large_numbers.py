def law_of_large_numbers(p1, p2):
    _, m, k = p1
    
    p2.sort()
    first = p2[-1]
    second = p2[-2]
    result = 0

    while True:
        for i in range(k):
            if m == 0:
                break
            result = result + first
            m = m - 1
        if m == 0:
            break            
        result = result + second
        m = m - 1

    return result
