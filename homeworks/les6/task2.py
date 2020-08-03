class Road(object):
    mass = 25
    depth = 5

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate(self):
        return self._length * self._width * Road.mass * Road.depth

print(Road(20, 5000).calculate())