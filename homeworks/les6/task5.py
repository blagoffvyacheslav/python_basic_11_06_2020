class Stationery(object):

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')

class Pen(Stationery):

    def draw(self):
        print('Запуск отрисовки {}'.format(self.title))

class Pencil(Stationery):

    def draw(self):
        print('Запуск отрисовки {}'.format(self.title))

class Handle(Stationery):

    def draw(self):
        print('Запуск отрисовки {}'.format(self.title))

a = Pen('ручкой')
b = Pencil('карандашом')
c = Handle('маркером')
