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

class Enemy:
    def __init__(self, x, y, width, height, end, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.velocity = 3
        self.walkCount = 0
        self.image = image

    def draw(self, canvas, cx = 0):
        canvas.create_image(self.x + cx, self.y - 30, image =
        ImageTk.PhotoImage(self.image))
        self.move()

    def move(self):
        if self.velocity > 0:
            if self.x  + self.velocity < self.path[1]:
                self.x += self.velocity
            else:
                self.velocity = self.velocity * -1
                self.walkCount = 0
        else:
            if self.x - self.velocity > self.path[0]:
                self.x += self.velocity
            else:
                self.velocity = self.velocity * -1
                self.walkCount = 0