sum = 0

with open('input_1.txt', 'rU') as fin:
    lst = fin.read()

    for i in range(0, len(lst)-1):
        if i == 0:
            prev = int(lst[i])
            start = int(lst[i])
            continue
        elif i == len(lst) - 2 and int(lst[i]) == start:
            sum += start
        else:
            if int(lst[i]) == prev:
                sum += prev
            prev = int(lst[i])
    print(sum)

    sum = 0

    rg = int((len(lst)-1)/2)
    for i in range(0, len(lst)-1-rg):
        if lst[i] == lst[i+rg]:
            sum += (int(lst[i]) * 2)

    print(sum)