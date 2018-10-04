d = {}
d_2 = {}
with open('input_13.txt', 'rU') as fin:
    for line in fin:
        a = line[:-1].split(': ')
        d[int(a[0])] = int(a[1])
        d_2[int(a[0])] = 0

step = 0
sum = 0
for i in range(0, 91):
    if i in d:
        inc = step/((d[i]-1)*2)
        if inc == 1.0 or inc == 2.0:
            print(i, d[i])
            sum += (i*d[i])
    step += 1

#print(sum)

#delay loop
for i in range(0, 3865118):
    #print(i)
    for key in d_2:
        d_2[key] += 1
        if d_2[key] == ((d[key]-1)*2+1):
            d_2[key] = 1

for i in range(0, 91):
    #print(i)
    for key in d_2:
        d_2[key] += 1
        if d_2[key] == ((d[key]-1)*2+1):
            d_2[key] = 1

    #print(d_2)
    if i in d_2:
        if d_2[i] == 1:
            print(i, d[i])



