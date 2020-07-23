a = input('Введите число a: ')
b = input('Веедите число b: ')
c = input('Веедите число c: ')

if not (a.isdigit() and b.isdigit() and c.isdigit()):
    raise TypeError('Введены не числа')



def my_func(a, b, c):
    digits = []
    digits.append(float(a))
    digits.append(float(b))
    digits.append(float(c))
    digits.sort(reverse=True)
    return sum(digits[0:2])
print(my_func(a,b,c))
