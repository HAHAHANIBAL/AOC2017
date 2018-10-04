with open('input_11.txt', 'rU') as fin:
    for item in fin:
        a = item[:-1].split(',')
start = [0, 0]
ma = []
#hex coordinates
for i in range(0, len(a)):
    if a[i] == 's':
        start[0] -= 1
    elif a[i] == 'n':
        start[0] += 1
    elif a[i] == 'se':
        start[1] -= 1
    elif a[i] == 'sw':
        start[0] -= 1
        start[1] += 1
    elif a[i] == 'nw':
        start[1] += 1
    elif a[i] == 'ne':
        start[0] += 1
        start[1] -= 1
    ma.append(start[0])


print(max(ma))
print(start)