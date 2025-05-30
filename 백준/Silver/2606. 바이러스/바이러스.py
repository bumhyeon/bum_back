import sys

input = sys.stdin.readline
#백준 2606번

from collections import deque, defaultdict

n = int(input())
s = int(input())
sajen = defaultdict(list)
for _ in range(s):
    key, value = map(int,input().split())

    sajen[key].append(value)
    sajen[value].append(key)

def bfs(b):
    visited = (n+1) * [False]
    queue = deque([b])
    visited[b] = True
    count = 0
    while queue:
        current = queue.popleft()
        for target in sajen[current]:   
            if not visited[target]:
                visited[target]=True
                count+=1
                queue.append(target)
    return count
print(bfs(1))