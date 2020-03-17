import pygame
import math
from projectiles.tear import Tear

class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.health = 6
        self.maxhealth = 6
        self.velocity = [0,0]
        self.maxvelocity = 8
        self.damages = 10
        #self.hitbox = pygame.Rect(10,10,50,50).
        self.image = pygame.image.load('assets/isaac.png')
        self.image = pygame.transform.scale(self.image,(100,120))
        self.hitbox = self.image.get_rect()
        self.all_projectiles = pygame.sprite.Group()
        self.tear_cd = 500
        self.temp = pygame.time.get_ticks()

    def position(self):
        if self.get_speed() >= self.maxvelocity:
            coef = self.get_speed()/self.maxvelocity
        else:
            coef = 1

        if self.hitbox.x > 10 and self.hitbox.x < 1200:
            self.hitbox.x += int(self.velocity[0]/coef)
        else:
            if self.hitbox.x < 500:
                self.hitbox.x = 11
                self.velocity[0] = 0
            if self.hitbox.x > 500:
                self.hitbox.x = 1199
                self.velocity[0] = 0

        if self.hitbox.y > 10 and self.hitbox.y < 640:
            self.hitbox.y += int(self.velocity[1]/coef)
        else:
            if self.hitbox.y < 500:
                self.hitbox.y = 11
                self.velocity[1] = 0
            if self.hitbox.y > 500:
                self.hitbox.y = 639
                self.velocity[1] = 0


    def shoot(self,direction):
        print("shoot")

        if (pygame.time.get_ticks()-self.temp)>self.tear_cd:
            self.all_projectiles.add(Tear(self,direction))
            self.temp = pygame.time.get_ticks()
        else:
            pass

        print("fin de shoot")

    def get_speed(self):

        return math.sqrt((self.velocity[0]**2)+(self.velocity[1]**2))

    def move_right(self,state):
        if state:
            print(str(self.velocity[0])+ ","+str(self.velocity[1]))
            if int(self.velocity[0]) < self.maxvelocity / 2:
                self.velocity[0] = self.maxvelocity / 2
            if self.velocity[0] < self.maxvelocity:
                self.velocity[0] += self.maxvelocity/30
        else:
            if self.velocity[0] > 0:
                self.velocity[0] -= self.maxvelocity/20

    def move_left(self,state):
        if state:
            if self.velocity[0] > -self.maxvelocity:
                self.velocity[0] -= 1
        else:
            if self.velocity[0] < 0:
                self.velocity[0] += 1

    def move_up(self,state):
        if state:
            if self.velocity[1] > -self.maxvelocity:
                self.velocity[1] -= 1
        else:
            if self.velocity[1] < 0:
                self.velocity[1] += 1

    def move_down(self,state):
        if state:
            if self.velocity[1] < self.maxvelocity:
                self.velocity[1] += 1
        else:
            if self.velocity[1] > 0:
                self.velocity[1] -= 1