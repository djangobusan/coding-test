def coin_split(total_value=0):
    count = 0
    coin_types = [500, 100, 50, 10]

    for coin in coin_types:
        count = count + (total_value // coin)
        total_value = total_value % coin

    return count


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


def count_with_three_in_time(h):
    count = 0
    # 계산
    for i in range(h + 1):
        for j in range(60):
            for k in range(60):
                if "3" in str(i) + str(j) + str(k):
                    count = count + 1
    return count


def k_knight(p):
    column = ord(p[0]) - ord('a') + 1
    row = int(p[1])
    steps = [(-2, -1), (-1, -2), (1, -2), (2, -1),
             (2, 1), (1, 2), (-1, 2), (-2, 1)]
    result = 0

    for step in steps:
        next_row = row + step[0]
        next_column = column + step[1]
        if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_row <= 8:
            result = result + 1

    return result


def __is_prime__(n):
    if n < 2: return False
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True


def find_prime(numbers):
    from itertools import permutations

    list_numbers = list(numbers)
    num = []
    num2 = []
    result = 0

    for i in range(1, len(list_numbers) + 1):
        num.append(list(permutations(list_numbers, i)))

    for i in num:
        for j in i:
            num2.append(int(''.join(j)))

    for i in num2:
        if __is_prime__(i):
            result = result + 1

    return result


if __name__ == '__main__':
    print(find_prime("17"))
