def bfs(graph, start, n):    # graph, 탐색 시작점, 정점개수
    visited = [0]*(n+1)
    queue = []
    queue.append(start)
    visited[start] = 1
    while queue:
        t = queue.pop(0)
        visit(t)
        for i in graph[t]:
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[n] + 1