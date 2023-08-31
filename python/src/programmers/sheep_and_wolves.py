# https://school.programmers.co.kr/learn/courses/30/lessons/92343

def sheep_and_wolves(info, edges):
    visited = [0] * len(info)
    visited[0] = 1
    answer = []

    def dfs(sheep, wolves):
        if sheep > wolves: answer.append(sheep)
        else: return

        for edge in edges:
            parent, child = edge
            wolf = info[child] == 1

            if visited[parent] and not visited[child]:
                visited[child] = 1
                dfs(sheep + (not wolf), wolves + wolf)
                visited[child] = 0
                
    dfs(1, info[0])
    return max(answer)
