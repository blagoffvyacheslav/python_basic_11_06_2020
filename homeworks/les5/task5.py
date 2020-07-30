with open('task5.txt', 'r') as file:
    s = 0
    for l in file:
        for el in l.split(' '):
            s+=int(el)
print('Сумма: ', s)