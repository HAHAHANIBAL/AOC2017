l = [i for i in range(256)]
l = list(map(str, l))

with open('input_10.txt', 'rU') as fin:
    for line in fin:
        a = line[:-1].split(',')
a = list(map(int, a))

start_pos = 0
skip_size = 0

for item in a:
    if start_pos+item <= len(l):
        if item == 1 or item == 0:
            remaining_length = len(l) - start_pos
            length = item + skip_size - remaining_length
            length = length % len(l)
            start_pos = length
            skip_size += 1
        else:
            rev = l[start_pos:(start_pos+item)]
            rem_1 = l[:start_pos]
            rem_2 = l[(start_pos+item):]
            #twisting
            rev = rev[::-1]
            l = rem_1 + rev + rem_2
            remaining_length = len(l) - start_pos
            length = item + skip_size - remaining_length
            length = length % len(l)
            start_pos = length
            skip_size += 1

    else:
        if item == 1:
            remaining_length = len(l) - start_pos
            length = item + skip_size - remaining_length
            length = length % len(l)
            start_pos = length
            skip_size += 1
        else:
            rev = l[start_pos:]+l[:(item-(len(l)-start_pos))]
            rem = l[(item-(len(l)-start_pos)):start_pos]
            rev = rev[::-1]
            idx = l.index(rem[-1])
            tmp = len(l)-idx
            rear = rev[:tmp-1]
            front = rev[tmp-1:]
            l = front + rem + rear
            remaining_length = len(l) - start_pos
            length = item + skip_size - remaining_length
            length = length % len(l)
            start_pos = length
            skip_size += 1

print(l)


