stacknum = int(input())
outback = []
recipe = []
result = []
j = 1

for _ in range(stacknum):
    outback.append(int(input()))

for num in outback:
    if j <= num:
        for i in range(j, num + 1):
            recipe.append(i)
            result.append("+")
        j = num + 1

    if recipe and recipe[-1] == num:
        recipe.pop()
        result.append("-")
    else:
        print("NO")
        exit()

print("\n".join(result))
