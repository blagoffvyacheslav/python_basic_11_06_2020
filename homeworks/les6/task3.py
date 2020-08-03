class Worker(object):

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = sum(income.values())

class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income

print(Position('Петров', 'Иван', 'Разработчик', {"wage": 5, "bonus": 1}).get_full_name())
print(Position('Сидоров', 'Василий', 'Разработчик', {"wage": 4 , "bonus": 0}).get_total_income())