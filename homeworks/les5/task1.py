with open('f.txt', 'a') as file:
    while True:
        l = input('Введите данные: ')
        file.write(l+'\n')
        if l == '':
            break