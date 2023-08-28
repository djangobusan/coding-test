def __is_prime__(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True
    
def find_prime(numbers):
    from itertools import permutations

    list_numbers = list(numbers)
    result = []
    num = []

    for i in range(1, len(list_numbers)+1):
        num.append(list(permutations(list_numbers, i)))

    num = [int("".join(j)) for i in num for j in i]

    for i in num:
        if __is_prime__(i):
            result.append(i)

    return len(set(result))
