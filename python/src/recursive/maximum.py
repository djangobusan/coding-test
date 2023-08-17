def maximum(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        m = maximum(lst[1:])
        return m if m > lst[0] else lst[0]
    
def tail_maximum(lst, acc=0):
    if lst == []:
        return acc
    else:
        return tail_maximum(lst[1:], acc if acc > lst[0] else lst[0])