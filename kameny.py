#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 10:01:32 2018

@author: vol35098
"""


import pyglet
import random
from math import sin, cos, radians, pi

window = pyglet.window.Window(1200, 800)         #rozlišení..okénko
batch = pyglet.graphics.Batch()                 #pro optimalizované vykreslování objektů


class Stone(object):                            #objektová třída
        def __init__(self, x = None, y = None, speed = None, direction = None):
          self.x = x or random.randint(0, window.width)
          self.y = y or random.randint(0, window.height)
          self.direction = direction or random.randint(0, 360)
          self.speed = speed or random.randint(30, 150)
          self.rspeed = random.randint(-40, 40)
          #načtu obrázek
          self.image = pyglet.image.load('meteors/1.png')
          #střed otáčení dám na střed obrázku
          self.image.anchor_x = self.image.width // 2           #přesunutí kotvy do středu
          self.image.anchor_y = self.image.height // 2          #přesunutí kotvy do středu vlastně směr otáčení (nastavení)
          #z obrázku vytvořím sprite
          self.sprite = pyglet.sprite.Sprite(self.image, batch = batch)             #objekt jehož zobrazování je optimalizované
          #správně nastavím souřadnice sprite
          self.sprite.x = self.x
          self.sprite.y = self.y
          
    
        def tick(self, dt):
            #do proměnné dt se uloží doba od posledního tiknutí
            self.x += dt * self.speed * cos(pi / 2 - radians(self.direction))
            self.sprite.x = self.x #definice self.x
            self.y += dt * self.speed * sin(pi / 2 - radians(self.direction))
            self.sprite.y = self.y #definice self.y
            self.sprite.rotation += self.rspeed


kameny = []            
for i in range(30):
    kamen = Stone()
    kameny.append(kamen)
    pyglet.clock.schedule_interval(kamen.tick, 1 / 30)

@window.event
def on_draw():
    window.clear()
    batch.draw()
    

pyglet.app.run()