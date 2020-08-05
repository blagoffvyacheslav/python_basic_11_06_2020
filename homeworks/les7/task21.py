from abc import ABC, abstractmethod

class Clothes(ABC):

    def __init__(self, size):
        self.__size = size

    @abstractmethod
    def calculate(self):
        pass
