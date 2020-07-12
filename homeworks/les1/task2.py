s = input('Введите секунды: ')
hh = mm = ss = 0

try:
    s = int(s)
except:
    print('Введеный строковый литерал не приводится к целому числу')
    exit()

hh = s // 60**2
ss = s % 60**2
if ss == 0:
    pass
else:
    mm = ss // 60
    ss = ss % 60

print("Часов, минут, секунд: {hh}:{mm}:{ss}".format(hh=hh,mm=mm,ss=ss))

