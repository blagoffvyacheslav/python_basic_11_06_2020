x = input('Введите число x: ')
y = input('Введите число y: ')


if float(x) > 0 and int(y) < 0:
    pass
else:
    raise TypeError('Нарушение условия')



def my_func(x, y):
    res = 1
    for _ in enumerate(range(abs(y))):
        res/=x
    return res

print(my_func(float(x),int(y)))
