start_sqr = 2
inc = 8
perimeter = 8
cnt = 1
flg = 1
num = 312051

while flg:
    start_sqr += (inc*cnt)
    perimeter += inc
    cnt += 1
    if start_sqr+perimeter > num:
        vert = cnt
        rmn = num-start_sqr
        median = (perimeter/4+1)/2+0.5
        dec = perimeter/4*4-rmn
        step = abs(median - dec) + vert
        flg = 0
print(step)

#neighbors
def check_coor(dict, x, y):
    if (x-1, y-1) in dict and (x, y) in dict:
        dict[x, y] += dict[x-1, y-1]
    elif (x-1, y-1) in dict and (x, y) not in dict:
        dict[x, y] = dict[x-1, y-1]

    if (x-1, y) in dict and (x, y) in dict:
        dict[x, y] += dict[x-1, y]
    elif (x-1, y) in dict and (x, y) not in dict:
        dict[x, y] = dict[x-1, y]

    if (x, y-1) in dict and (x, y) in dict:
        dict[x, y] += dict[x, y-1]
    elif (x, y-1) in dict and (x, y) not in dict:
        dict[x, y] = dict[x, y-1]

    if (x+1, y-1) in dict and (x, y) in dict:
        dict[x, y] += dict[x+1, y-1]
    elif (x+1, y-1) in dict and (x, y) not in dict:
        dict[x, y] = dict[x+1, y-1]

    if (x-1, y+1) in dict and (x, y) in dict:
        dict[x, y] += dict[x-1, y+1]
    elif (x-1, y+1) in dict and (x, y) not in dict:
        dict[x, y] = dict[x-1, y+1]

    if (x+1, y+1) in dict and (x, y) in dict:
        dict[x, y] += dict[x+1, y+1]
    elif (x+1, y+1) in dict and (x, y) not in dict:
        dict[x, y] = dict[x+1, y+1]

    if (x, y+1) in dict and (x, y) in dict:
        dict[x, y] += dict[x, y+1]
    elif (x, y+1) in dict and (x, y) not in dict:
        dict[x, y] = dict[x, y+1]

    if (x+1, y) in dict and (x, y) in dict:
        dict[x, y] += dict[x+1, y]
    elif (x+1, y) in dict and (x, y) not in dict:
        dict[x, y] = dict[x+1, y]
    return dict

num = 312051
x = 0
y = 0
d = {}
d[x,y] = 1
perimeter = 8
inc = 8
flg = 1
#movement
while flg:
    for i in range(1, perimeter+1):
        if i == 1:
            x += 1
            d = check_coor(d, x, y)
        elif 1 < i <= perimeter/4:
            y += 1
            d = check_coor(d, x, y)
        elif perimeter/4 < i <= perimeter/4 * 2:
            x -= 1
            d = check_coor(d, x, y)
        elif perimeter/4 * 2 < i <= perimeter/4 * 3:
            y -= 1
            d = check_coor(d, x, y)
        elif perimeter/4 * 3 < i <= perimeter:
            x += 1
            d = check_coor(d, x, y)
        maximum = max(d, key=d.get)
        if d[maximum] > num:
            print(d[maximum])
            flg = 0
            break
    perimeter += inc
