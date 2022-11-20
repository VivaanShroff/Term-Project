#Term Project Graphics
from cmu_112_graphics import *

import math, random

from NewTermProject import *

#Referenced from Sidescroller from Animations Part 4 Notes.
def appStarted(app):
    app.scrollX = 0
    app.dots = [(random.randrange(4*app.width//5, app.width),
                random.randrange(60, app.height))]
    app.r = 20
    app.jump = False
    app.velocityY = 0
    app.posX = app.width
    app.beginVelo = -30
    app.posY = app.height - 10
    app.baseY = app.posY
    app.isGameOver = False
    app.rectangle = Rectangle(app.posX, app.posY, 'Red')
    app.bullets = Bullet(app.posX, app.posY, 'Black')
    app.imageog = app.loadImage('cartoon-map-bear-baby-clipart-png-image.png')
    app.image = app.scaleImage(app.imageog, 1/10)

def timerFired(app):
    if app.isGameOver == False:
        app.scrollX += 10
        app.posX += app.scrollX
        if app.jump:
            app.posY += app.velocityY
            app.velocityY += 5
            if app.posY == app.baseY:
                app.jump = False
        app.dots += [(random.randrange(app.posX, app.posX + 10),
                random.randrange(3*app.height/4, app.height))]
    
def keyPressed(app, event):
    if app.isGameOver == False:
        if (event.key == "Right"): app.scrollX += 15
        if (event.key == "Up") and app.jump == False:
            app.velocityY = app.beginVelo
            app.jump = True

def redrawAll(app, canvas):
    canvas.create_image(app.width//6, app.posY - app.r/2, image = 
    ImageTk.PhotoImage(app.image))
    canvas.create_rectangle(0, app.height, app.width, app.height - 10, fill =
    'black')
    for (cx, cy) in app.dots:
        cx -= app.scrollX
        canvas.create_oval(cx-10, cy-10, cx+10, cy+10, fill='lightGreen')
        app.rectangle.draw(canvas, cx)
        app.bullets.draw(canvas, cx)

#class Animal:
#     def __init__(self):
#         self.x = 60
#         self.y = 0
#         self.yvelocity = 0
#         self.height = 40
#         self.width = 20
#     def jump(self):
#         if self.y == 0:
#             self.yvelocity = 300
#     def update(self, deltaTime):
#         self.yvelocity += -500 * deltaTime
#         self.y += self.yvelocity * deltaTime
#         if self.y < 0:
#             self.y = 0
#             self.yvelocity = 0

def main():
    runApp(width = 800, height = 400)

if __name__ == '__main__':
    main()