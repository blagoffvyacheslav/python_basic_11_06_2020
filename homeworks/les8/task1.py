class Date(object):
    date = ''
    months = ('январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь', 'несуществующий')
    months = {item:idx for idx, item in enumerate(months, 1)}

    def __init__(self, date):
        Date.date = date

    @classmethod
    def m1(cls):
        parts = cls.date.split('-')
        try:
            parts[1] = cls.months[parts[1]]
        except ValueError('Указан неверно месяц'):
            exit()
        return int(''.join([str(elem) for elem in parts]))

    @staticmethod
    def m2():
        parts = Date.date.split('-')
        if not 1 <= Date.months[parts[1]] <=12:
            raise ValueError('Несуществующий месяц')

if __name__ == '__main__':
    d1 = Date('05-декабрь-1994')
    print(d1.m1())
    d1.m2()
    d2 = Date('05-несуществующий-1994')
    print(d2.m1())
    d2.m2()