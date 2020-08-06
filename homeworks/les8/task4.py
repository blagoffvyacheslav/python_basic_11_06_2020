class Storage(object):

    goods = []

    def __init__(self):
        pass

    @classmethod
    def acceptance(cls, good):
        if isinstance(good, Inventory):
            if isinstance(good, Printer):
                if isinstance(good.quantity, str):
                    raise TypeError('Количество для приема на склад принтеров указано неверно!')
            prod = {key:value for key,value in good.__dict__.items()}
            cls.goods.append(prod)

class Inventory(object):

    def __init__(self, name, quantity):
        self.__name = name
        self.__quantity = quantity

    @property
    def name(self):
        return self.__name

    @property
    def quantity(self):
        return self.__quantity

class Printer(Inventory):

    def __init__(self, *args, pages):
        self.__pages = pages
        super().__init__(*args)

    @property
    def pages(self):
        return self.__pages


class Scanner(Inventory):

    def __init__(self, *args, capture_area):
        self.__capture_area = capture_area
        super().__init__(*args)

    @property
    def capture_area(self):
        return self.__capture_area


class Xerox(Inventory):

    def __init__(self, *args, dpi):
        self.__dpi = dpi
        super().__init__(*args)

    @property
    def dpi(self):
        return self.__dpi


if __name__ == '__main__':
    s = Printer('принтер', 3, pages = 3)
    p = Scanner('сканер', 7, capture_area = 2)
    x = Xerox('ксерокс', 4, dpi = 6)
    storage = Storage()
    storage.acceptance(s)
    storage.acceptance(p)
    storage.acceptance(x)
    print(storage.goods)
