from task21 import Clothes
class Coat(Clothes):

    def __init__(self, size):
        self.__size = size

    def calculate(self):
        return self.__size / 6.5 + 0.5

class Suit(Clothes):

    def __init__(self, size):
        self.__size = size

    def calculate(self):
        return 2 * self.__size + 0.3

class Total(object):

    def __init__(self, s1: Clothes, s2: Clothes):
        self.__s1 = s1
        self.__s2 = s2

    @property
    def s1(self):
        return self.__s1

    @property
    def s2(self):
        return self.__s2

    def total(self):
        print(self.s1.calculate() + self.s2.calculate())


a = Coat(3)
a.calculate()
b = Suit(4)
b.calculate()
c = Total(a,b)
c.total()
