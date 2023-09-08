from math import sqrt
from aiogram import bot


class Point():
    def __init__(self, x, y):
        self.x = x 
        self.y = y
    
    def get_length(self):
        return sqrt(self.x ** 2 + self.y ** 2)


