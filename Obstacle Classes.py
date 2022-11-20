from cmu_112_graphics import *

import math, random

class Obstacle:
    def __init__(self, width, height, color):
        self.x1 = width
        self.y1 = height
        self.color = color
        self.slider = 10

class Rectangle(Obstacle):
    def __init__(self, width, height, color):
        super().__init__(width, height, color)
        self.x2R = width + 10
        self.y2R = height - 30
    def draw(self, canvas, cx=0):
        canvas.create_rectangle(self.x1+cx, self.y1, self.x2R+cx, self.y2R,
        fill=self.color)

class Bullet(Obstacle):
    def __init__(self, width, height, color):
        super().__init__(width, height, color)
        self.x2B = width + 10
        self.y2B = height - 10
    def draw(self, canvas, cx = 0):
        canvas.create_oval(self.x1+cx, self.y1 + random.randint(-10, 10),
        self.x2B+cx, self.y2B + random.randint(-10, 10), fill = self.color)