my_list = [7, 5, 3, 3, 2]
n = input('Введите новый элемент рейтинга: ')
try:
    n = int(n)
except TypeError('Введено не число'):
    exit()


def reverse_numeric(x, y):
    return y - x

my_list.append(n)
my_list.sort(reverse=True)

print('Пользователь ввел число ', n, ' результат,',my_list)