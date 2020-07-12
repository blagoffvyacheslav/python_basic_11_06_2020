n = input('Введите положительное число: ')
try:
    n = int(n)
    if not n>0:
        raise ValueError('Число неположительное')
except Exception as error:
    print(error)
    exit()

print('Введеное число: ', n)
max = int(str(n)[0])
while (n // 10 != 0):
    q = n % 10
    if q>max:
        max = q
    n = n // 10

print('Max is: ', max)
