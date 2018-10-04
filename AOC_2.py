sum = 0

with open('input_2.txt', 'rU') as fin:
    lst = fin.read()
    array = []
    num = ''
    for i in range(0, len(lst)):
        if lst[i] == '\t':
            array.append(int(num))
            num = ''
        elif lst[i] == '\n':
            array.append(int(num))
            ma = max(array)
            mi = min(array)
            sum += (ma - mi)
            num = ''
            array = []
        else:
            num += lst[i]

    print(sum)

    sum = 0
    array = []
    num = ''
    for i in range(0, len(lst)):
        if lst[i] == '\t':
            array.append(int(num))
            num = ''
        elif lst[i] == '\n':
            array.append(int(num))
            mi = min(array)
            array.remove(mi)
            flg = 1
            while flg:
                for item in array:
                    if item % mi == 0:
                        sum += (item/mi)
                        flg = 0
                        break
                mi = min(array)
                array.remove(mi)
            num = ''
            array = []
        else:
            num += lst[i]

    print(sum)