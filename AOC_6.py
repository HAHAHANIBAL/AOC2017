with open('input_6.txt', 'rU') as fin:
    for line in fin:
        key = line[:-1].split('\t')

key = list(map(int, key))
flg = 1
a = []
#cycles
cnt = 0
while flg:
    ma = max(key)
    #automatically chose the first max value in the list
    idc = key.index(ma)
    #reset
    key[idc] = 0
    for i in range(0, ma):
        if idc < len(key) - 1:
            idc += 1
        else:
            idc = 0
        key[idc] += 1
    #can't use int list to compare in Python
    key_a = list(map(str, key))

    if key_a not in a:
        a.append(key_a)
    else:
        loop_idc = a.index(key_a)
        print(cnt-loop_idc)
        flg = 0

    cnt += 1
print(cnt)

