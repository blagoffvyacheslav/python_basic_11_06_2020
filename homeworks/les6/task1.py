from itertools import cycle
import time

class TrafficLight(object):

    def __init__(self, colour, seconds):
        self.__colour = colour
        self.seconds = seconds

    def running(self):
        print('Светофор переключен на', self.__colour)
        time.sleep(self.seconds)

if __name__ == "__main__":
    colours = [('красный', 7), ('желтый', 2), ('зеленый', 8)]
    for _ in  cycle(colours):
        TrafficLight(*_).running()