def my_func(*args):
    s = 0
    for el in args:
        if el.isdigit():
            s+=float(el)
        elif el == 'q':
            return s
    return s
s = 0
while True:
    line = input('Введите числа через запятую или введите q для выхода: ')
    if line == 'q':
        break
    line = line.split(' ')
    s += my_func(*line)
    print('Сумма: ', s)

