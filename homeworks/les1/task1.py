a  = 'Переменная a'
b  = 'Переменная b'
c1 = '1'
d2 =  2
print(a)
print(b)
print(c1)
print(d2)
e = input('Введите текст: ')
f = input('Введите число: ')

print(e)
try:
    print(float(f))
except:
    print('Введеный строковый литерал не приводится к вещественному числу')