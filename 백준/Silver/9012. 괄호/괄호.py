T = int(input())

for _ in range(T):
    garo = input()
    rcnt = 0
    lcnt = 0
    rlist = []
    llist = []
    
    if garo[0] == ')' or garo[-1] == '(' or len(garo) < 2:
        print('NO')
        continue

    for i in garo:
        if i == '(':
            rcnt += 1
            rlist.append(rcnt)
        elif i == ')':
            lcnt += 1
            llist.append(lcnt)
            if rcnt > 0:
                rcnt -= 1
            else:
                print('NO')
                break
    else:
        if rcnt == 0:
            print('YES')
        else:
            print('NO')
