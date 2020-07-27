n = input('Введите n: ')
try:
    n = int(n)
except ValueError:
    print('Неверное значение')
    exit()
def fact(n):
    l = [el for el in range(1, n+1)]
    for el in l:
        yield el

gen = fact(n)
while True:
    try:
        print(gen.__next__())
    except StopIteration:
        print('Достигнут конец генератора')
        exit()