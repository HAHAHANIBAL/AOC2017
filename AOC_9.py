rank = 1
score = 0
int_cnt = 0
flg = 1
i = 1
sum_ga = 0
ga_cnt = 0
with open('input_9.txt', 'rU') as fin:
    a = fin.read()

while flg:
    if a[i] == '{':
        if a[i-1] == '!':
            i += 1
        else:
            rank += 1
            i += 1
    elif a[i] == '}':
        if a[i-1] == '!':
            i += 1
        else:
            score += rank
            rank -= 1
            i += 1
    elif a[i] == '<':
        if a[i-1] == '!':
            i += 1
        else:
            flg_2 = 1
            while flg_2:
                i += 1
                ga_cnt += 1
                if a[i] == '!':
                    ga_cnt -= 1
                    i += 1
                elif a[i] == '>':
                    flg_2 = 0
                    i += 1
                    ga_cnt -= 1
                    sum_ga += ga_cnt
                    ga_cnt = 0
    else:
        i += 1
    if i == len(a):
        flg = 0


print(score)
print(sum_ga)
