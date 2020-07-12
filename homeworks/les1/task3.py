n = input('Введите число: ')
n = str(n)


# n + nn + nnn


n1 = int(n)
n2 = int(n*2)
n3 = int(n*3)

s = 0
for el in [n1, n2, n3]:
    s = s + el

print('Сумма n+nn+nnn=', s)
