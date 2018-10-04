d = {}
ma = 0
with open('input_8.txt', 'rU') as fin:
    for line in fin:
        a = line[:-1].split(' ')
        w_1 = a[0]
        w_2 = a[4]

        #initiate registration
        if w_1 not in d:
            d[w_1] = 0
        if w_2 not in d:
            d[w_2] = 0

        #first judge w_2
        if a[5] == '==':
            if d[w_2] == int(a[6]):
                flg = 1
            else:
                flg = 0
        elif a[5] == '>':
            if d[w_2] > int(a[6]):
                flg = 1
            else:
                flg = 0
        elif a[5] == '<':
            if d[w_2] < int(a[6]):
                flg = 1
            else:
                flg = 0
        elif a[5] == '!=':
            if d[w_2] != int(a[6]):
                flg = 1
            else:
                flg = 0
        elif a[5] == '>=':
            if d[w_2] >= int(a[6]):
                flg = 1
            else:
                flg = 0
        elif a[5] == '<=':
            if d[w_2] <= int(a[6]):
                flg = 1
            else:
                flg = 0

        if a[1] == 'inc' and flg == 1:
            d[w_1] += int(a[2])
            if ma < d[w_1]:
                ma = d[w_1]
        elif a[1] == 'dec' and flg == 1:
            d[w_1] -= int(a[2])
            if ma < d[w_1]:
                ma = d[w_1]

print(d[max(d,key=d.get)])
print(ma)