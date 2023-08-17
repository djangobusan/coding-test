def count_with_three_in_time(h):
    count = 0
    for i in range(h+1):
        for j in range(60):
            for k in range(60):
                if "3" in str(i) + str(j) + str(k):
                    count = count + 1
    return count