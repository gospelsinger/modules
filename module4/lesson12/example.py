def dfs(graph, vertex, visited):
    if vertex not in visited:
        print(vertex, end = ' ')
        visited.append(vertex)
        for neighbor in graph[vertex]:
            dfs(graph, neighbor, visited)

# Пример использования:
graph = {
    0: [1, 3],
    1: [0, 2, 3],
    2: [1, 3],
    3: [0, 1, 2],
}

visited = []
dfs(graph, 0, visited)