d = {}
with open('input_12.txt', 'rU') as fin:
    for line in fin:
        temp = line[:-1].split(' <-> ')
        e = temp[1].split(', ')
        e = list(map(int, e))
        d[int(temp[0])] = e

group = []
group_agg = []
key = 0

#recursion
def find_group(key, group, d):
    for item in d[key]:
        if item not in group:
            group.append(item)
            find_group(item, group, d)
    return(group)

group = find_group(key, group, d)
print(len(group))

group = []
group_cnt = 0
for key in d:
    if key not in group_agg:
        group = find_group(key, group, d)
        for item in group:
            group_agg.append(item)
        group_cnt += 1
    group = []
print(group_cnt)

#iteration
#cnt = 0
#flg = 1
#while flg:
#    for key in range(0, len(d)):
#        if key in group_key:
#            for item in d[key]:
#                if item not in group_key:
#                    group_key.append(item)
#    cnt += 1
#    if cnt > 20:
#        flg = 0
#        break
#print(len(group_key))


