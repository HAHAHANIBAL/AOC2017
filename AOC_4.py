
d = {}
cnt = 0
with open('input_4.txt','rU') as fin:
    for line in fin:
        key = line[:-1].split(' ')
        for item in key:
            if item not in d:
                d[item] = 1
            else:
                break
        if len(d) == len(key):
            cnt += 1
        d = {}

print(cnt)

d = {}
num = 1
word_sum = 0
temp_array = []
cnt = 0
with open('input_4.txt','rU') as fin:
    for line in fin:
        key = line[:-1].split(' ')
        for item in key:
            for i in range(0, len(item)):
                if item[i] not in d:
                    d[item[i]] = num
                    word_sum += num
                    #this part is tricky, there should be better way to solve this rather than using hash table
                    num *= 2
                else:
                    word_sum += d[item[i]]

            if word_sum in temp_array:
                word_sum = 0
                break
            else:
                temp_array.append(word_sum)
                word_sum = 0

        if len(temp_array) == len(key):
            cnt += 1
        temp_array = []
print(cnt)