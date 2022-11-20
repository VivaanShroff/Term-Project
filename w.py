from cmu_112_graphics import *

def appStarted(app):
    spritestrip = app.loadImage('https://www.kindpng.com/picc/m/226-2266291_enemy-sprite-sheet-sprite-sheet-enemy-png-transparent.png')
    app.sprites = []
    for i in range(3):
        sprite = spritestrip.crop((30+260*i, 0, 230 + 260*i, 500))
        app.sprites.append(sprite)
    app.spriteCounter = 0

def timerFired(app):
    app.spriteCounter = (1 + app.spriteCounter) % len(app.sprites)

def redrawAll(app, canvas):
    sprite = app.sprites[app.spriteCounter]
    app.another = Zombie(ImageTk.PhotoImage(sprite))

class Zombie:
    def __init__(self, sprite):
        self.image = sprite
    def draw(self, canvas):
        canvas.create_image(200, 200, image = self.image)