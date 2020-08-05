class Matrix (object):

    def __init__(self, matrix=None):
        if matrix:
            self.__m = matrix
        else:
            self.__m = []
            i = 1
            while True:
                el = input('Введите значения матрицы через пробел. Для перехода на другую строку нажмите ВВОД, а для завершения заполнения наберите q: ').format(i)
                if el == 'q':
                    break
                self.__m.append([int(item) for item in el.split(' ') if item.isdigit()])

    def __str__(self):
        s = str()
        for row in self.__m:
            s += ' '.join([str(elem) for elem in row]) + '\n'
        return s

    def __add__(self, other):
        if isinstance(other, Matrix):
            m = []
            for el1, el2 in zip(self.__m, other.__m):
                s = []
                for e1, e2 in zip(el1, el2):
                    s.append(e1+e2)
                m.append(s)
            new = Matrix(m)
            return new
        else:
            raise TypeError('Дан объект не типа Matrix')


if __name__ == '__main__':
    a = Matrix()
    b = Matrix()
    print(a)
    print(b)
    print(a + b)