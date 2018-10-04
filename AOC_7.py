#easier with regex but I don't want to use libraries
a_con = []
a_ano = []
t = {}
wght = {}
with open('input_7.txt', 'rU') as fin:
    for line in fin:
        a = line[:-1].split(' ')
        a_con.append(a[0])
        wght[a[0]] = int(a[1].strip('()'))
        if '->' in a:
            t[a[0]] = []
            arr_idc = a.index('->')
            for i in range(arr_idc + 1, len(a)):
                stp = a[i].strip(',')
                t[a[0]].append(stp)
                a_ano.append(stp)
root = list(set(a_con) - set(a_ano))

#print(wght)
#find child
def is_child_equal(item, t, wght):
    #a = len(t)
    sum = 0
    for key in t:
        div = wght[key]
        sum += wght[key]
        print(sum)
    if sum % div == 0:
        wght[item] += sum
        return wght
    else:
        return 0

def find_child(root, t, wght):
    for item in root:
        if item in t:
            find_child(t[item], t, wght)
            wght = is_child_equal(item, t[item], wght)
            print(item)
            print(t[item])

find_child(['xegshds'], t, wght)
#it return error but it's a quick and dirty way to find the problematic node