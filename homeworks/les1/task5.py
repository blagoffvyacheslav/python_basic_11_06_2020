revenue = input('Введите выручку: ')
costs = input('Введите издержки: ')
try:
    revenue = float(revenue)
    costs = float(costs)
except Exception as error:
    exit()

if revenue > costs:
    profit = revenue - costs
    print('Фирма работает с приылью ', profit)
    print('Рентабельность выручки ', profit / revenue)
    try:
        persones = int(input('Введите количество сотрудниников: '))
    except:
        print('Количество должно быть числом')
    print('Прибыль в расчете на одного сотрудника ', profit/persones)
elif revenue < costs:
    print('Фирма работает с убытком')