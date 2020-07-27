import sys

try:
    hours = sys.argv[1]
    rate = sys.argv[2]
    prize = sys.argv[3]
except IndexError:
    print('Константы не даны')
    exit()

try:
    hours = float(hours)
    rate = float(rate)
    prize = float(prize)
except ValueError:
    print('Введены не числа')
    exit()

total = hours * rate + prize
print('Всего начислено ',total)