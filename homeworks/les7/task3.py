class Cell(object):

    def __init__(self, q):
        self.__q = q

    @property
    def cells_q(self):
        return self.__q

    def __add__(self, other):
        return Cell(self.cells_q + other.cells_q)

    def __sub__(self, other):
        delta = self.cells_q - other.cells_q
        if delta < 0:
            raise ValueError('Ошибка вычитания клеток')
        return Cell(delta)

    def __mul__(self, other):
        return Cell(self.cells_q * other.cells_q)

    def __truediv__(self, other):
        return Cell(self.cells_q // other.cells_q)

    def make_order(self, n):
        rows = self.cells_q // n
        surplus = self.cells_q % n
        return '\n'.join(['*'] * n + '*' * surplus if i + 1 == rows and surplus else '*' * n for i in range(rows))

if __name__ == '__main__':
    c1 = Cell(1)
    c2 = Cell(3)
    c3 = Cell(2)
    print(c2-c1)