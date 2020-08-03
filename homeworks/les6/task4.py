class Car(object):

    def __init__(self, speed, color, name, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, side):
        if side in ['налево', 'направо']:
            print('Машина повернула на {}'.format(side))
        else:
            raise ValueError('Сторона не указана корректно')

    def show_speed(self):
        return self.speed

class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            raise ValueError('Превышена скорость')

class SportCar(Car):
    pass

class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            raise ValueError('Превышена скорость')

class PoliceCar(Car):
    def __init__(self, *args, **kwargs):
        self.is_police = True
        super().__init__(args, kwargs)
