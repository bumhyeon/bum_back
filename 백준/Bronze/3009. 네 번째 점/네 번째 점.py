aa = []
al = set()
ala = set()
bb = []
bl = set()
blb = set()

for i in range(3):
    a, b= input().split()
    aa.append(a)
    bb.append(b)

for k in aa:
    if k in al:
        ala.add(k)
    al.add(k)
    
for j in bb:
    if j in bl:
        blb.add(j)
    bl.add(j)
ra = (al-ala).pop()
rb = (bl-blb).pop()

print(ra,rb)