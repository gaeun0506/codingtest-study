import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
people1, people2 = map(int, input().split())
m = int(input())

graph = [[] for i in range(n + 1)]
for i in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n + 1)

def dfs(node):
    for i in graph[node]:
        if visited[i] == 0:
            visited[i] = visited[node] + 1
            dfs(i)

dfs(people1)
print(visited[people2] if visited[people2] > 0 else -1)