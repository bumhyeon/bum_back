# 백준 1260번 DFS

Vertax, repeat_num, start = map(int, input().split())
dicti = {}

for i in range(1,Vertax+1):
    dicti[i] = []

for j in range(repeat_num):
    key, value = map(int, input().split())
    dicti[key].append(value)
    dicti[value].append(key)

for k in dicti:
    dicti[k].sort()

visited = [False] * (Vertax + 1)

def dfs(v):
    visited[v] = True
    print(v,end=' ')
    for l in dicti[v]:
        if not visited[l]:
            dfs(l)

dfs(start)
print()
from collections import deque   

visited_bfs = [False] * (Vertax + 1)
def bfs(b):
    queue = deque()
    queue.append(b)
    visited_bfs[b] = True
    while queue:
        now = queue.popleft()
        print(now, end = ' ')
        for u in dicti[now]:
            if not visited_bfs[u]:
                visited_bfs[u] = True
                queue.append(u)

bfs(start)