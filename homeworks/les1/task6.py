first_day_km = input('Введите км в первый день: ')
n_day_km = input('Введите km, не менее которого должно быть на n день: ')
try:
    first_day_km = float(first_day_km)
    n_day_km = float(n_day_km)
except Exception as error:
    exit()

n = 1
current_km = first_day_km
while current_km<=n_day_km:
    n+=1
    current_km*=1.1
    print('{n}-й день: {current_km:.2f}'.format(n=n, current_km=current_km))

print('на {n}-й день спортсмен достиг результата — не менее {n_day_km} км.'.format(n=n, n_day_km=n_day_km))

