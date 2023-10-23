from collections import deque

graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": ["F"], "F": []}

visited = set()


# 재귀 방법 사용
def recursion_dfs(visited_node, graph_node, node):
    if node not in visited_node:
        print(node)
        visited_node.add(node)
        for neighbor in graph_node[node]:
            recursion_dfs(visited_node, graph_node, neighbor)
    return visited_node


# 스택 방법 사용
def stack_dfs(visited_node, graph_node, start):
    stk = deque([start])

    while stk:
        node = stk.pop()
        if node not in visited_node:
            print(node)
            visited_node.add(node)
            stk.extend(set(graph_node[node]) - visited_node)
    return visited_node

def bfs(graph, root):


stack_dfs(visited, graph, "A")
