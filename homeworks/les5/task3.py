with open('task3.txt', 'r') as file:
    s = 0
    lastnames = []
    for i, l in enumerate(file, 1):
        try:
            last_name, wage = l.split(' ')
        except TypeError:
            print('Строка некорректная')
        try:
            wage = int(wage)
        except ValueError:
            print('Введена не зарплата')
        s += wage
        if wage < 20000:
            lastnames.append(last_name)
if i>1:
    s = s/i
print('Средняя зп: ', s)
print('Лица с зп меньше 20000: ', lastnames)