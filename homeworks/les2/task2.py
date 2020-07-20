l = []
n = input('Введите количество элементов: ')
try:
    n = int(n)
except TypeError:
    exit()
i=0
while i<=(n-1):
    l.append(input('Введите значение {i}: '.format(i=i)))
    i = i+1
for i, el in enumerate(l):
    if (i+1) % 2 == 0:
        l[i-1], l[i] = l[i],l[i-1]

for el in l:
    print(el)

