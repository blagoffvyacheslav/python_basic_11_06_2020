class MyTypeError(Exception):

    def __init__(self, txt):
        self.txt = txt

if __name__ == '__main__':
    l = []
    while True:
        el = input('Введите число или stop для завершения: ')
        try:
            if el == 'stop':
                break
            if el.isdigit():
                l.append(el)
            else:
                raise MyTypeError('Дано не число')
        except MyTypeError as error:
            print(error)
    print(l)