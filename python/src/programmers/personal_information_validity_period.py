# https://school.programmers.co.kr/learn/courses/30/lessons/150370

def day_to_num(day):
    year, month, day = tuple(day.split("."))
    return (int(year) * 28 * 12) + (int(month) * 28) + int(day)

def personal_information_validity_period(today, terms, privacies):
    answer = []
    sum_of_today = day_to_num(today)

    term = {}
    for i in terms:
        temp = i.split()
        term[temp[0]] = temp[1]

    for i,agreement in enumerate(privacies):
        agreement_date, agreement_type = agreement.split()
        sum_of_term = day_to_num(agreement_date)
        if (int(term[agreement_type]) * 28) <= abs(sum_of_term - sum_of_today):
            answer.append(i+1)

    return answer