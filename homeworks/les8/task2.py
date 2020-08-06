class DivError(Exception):

    def __init__(self, txt):
        self.txt = txt

if __name__ == '__main__':
    a = input('Введите a: ')
    b = input('Веедите b: ')
    if float(b) == 0:
        raise DivError('Ошибка деления ну нуль')
    else:
        print(float(a)/float(b))