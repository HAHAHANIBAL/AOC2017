a = []
with open('input_5.txt', 'rU') as fin:
    for line in fin:
        a.append(int(line[:-1]))

flg = 1
start = 0
while flg:
    step = a[start]
    a[start] += 1
    start = start + step
    if start >= len(a) or start < 0:
        break
    flg += 1

print(flg)

a = []
with open('input_5.txt', 'rU') as fin:
    for line in fin:
        a.append(int(line[:-1]))
flg = 1
start = 0

while flg:
    step = a[start]
    if a[start] >= 3:
        a[start] -= 1
    else:
        a[start] += 1
    start = start + step
    if start >= len(a) or start < 0:
        break

    flg += 1

print(flg)