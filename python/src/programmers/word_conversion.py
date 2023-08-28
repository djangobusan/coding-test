from collections import deque

def word_conversion(begin, target, words):
    queue = deque()
    queue.append([begin, 0])
    visitied = [0] * len(words)

    # 계산
    while queue:
        word, cnt = queue.popleft()
        if word == target: return cnt
        for i in range(len(words)):
            if not visitied[i]:
              if sum(x != y for x, y in zip(word, words[i])) == 1:
                   queue.append([words[i], cnt +1])
                   visitied[i] = 1
    return 0

