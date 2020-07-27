from itertools import cycle
import sys
try:
    mode = sys.argv[1]
except IndexError:
    print('Не задан параметр с режимом')
    exit()
if mode == str(1):
    def func(n1):
        l = [el for el in range(n1, 11)]
        for el in l:
            yield el
    n1 = input('Введите число, с которого будет задан генератор: ')
    try:
        n1 = int(n1)
    except ValueError:
        print('Введено не число')
        exit()

    gen = func(n1)
    while True:
        try:
            print(gen.__next__())
        except StopIteration:
            print('Достигнут конец генератора')
            exit()
elif mode == str(2):
    def repeat(l):
        print(l)
        el = input('Введите число или q для выхода: ')
        if el =='q':
            exit()
        try:
            el = int(el)
        except ValueError:
            print('Введено не число')
            exit()
        l.append(el)

    l = []
    repeat(l)
    for item in cycle(l):
        repeat(l)
else:
    raise InterruptedError('Введен неверный режим')