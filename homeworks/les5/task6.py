d = {}
with open('task6.txt', 'r') as file:
    for l in file:
        l = l.split(' ')
        s1 = 0
        for el in l[1:]:
            s = str()
            for i in el:
                if i.isdigit():
                    s+=i
            print(s)
        s1 += int(s)
            # s1+=int(s)
            # print(s1)
        d[l[0][:-1]] = l[0][:-1]


print(d)