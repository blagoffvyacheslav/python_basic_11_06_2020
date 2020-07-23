def operation(a,b):
    try:
        return a/b
    except Exception:
        print('Деление на нуль не определено')
        exit()

a = input('Введите число a: ')
b = input('Веедите число b: ')

if not (a.isdigit() and b.isdigit()):
    raise TypeError('Введены не числа')

print(operation(float(a),float(b)))