def take(n, lst_of):
    if n <= 0:
        return []
    if lst_of == []:
        return []
    else:
        return [lst_of[0]] + take(n-1, lst_of[1:])
    
def tail_take(n, lst_of, acc=[]):
    if n <= 0:
        return acc
    if lst_of == []:
        return acc
    else:
        return tail_take(n - 1, lst_of[1:], acc + [lst_of[0]])