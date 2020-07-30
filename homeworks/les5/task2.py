with open('task2.txt', 'r') as file:
    l = 0
    d = {}
    for i, l in enumerate(file, 1):
        d[str(i)+'-я строка'] = len(l.split(' '))
        l+=l
print(d)