import sys

n = int(sys.stdin.readline())
stack = []
output = []

for _ in range(n):
    cmd = sys.stdin.readline().split()

    if cmd[0] == "push":
        stack.append(int(cmd[1]))
    elif cmd[0] == "pop":
        output.append(stack.pop() if stack else -1)
    elif cmd[0] == "size":
        output.append(len(stack))
    elif cmd[0] == "empty":
        output.append(0 if stack else 1)
    elif cmd[0] == "top":
        output.append(stack[-1] if stack else -1)

print('\n'.join(map(str, output)))
