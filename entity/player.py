import pygame
import math

class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.health = 6
        self.maxhealth = 6
        self.velocity = [0,0]
        self.maxvelocity = 15
        self.damages = 10
        self.hitbox = pygame.Rect(10,10,50,50)


    def position(self):
        if self.get_speed() >= self.maxvelocity:
            coef = self.get_speed()/self.maxvelocity
        else:
            coef = 1
        self.hitbox.x += self.velocity[0]/coef
        self.hitbox.y += self.velocity[1]/coef


    def get_speed(self):

        return math.sqrt((self.velocity[0]**2)+(self.velocity[1]**2))

    def move_right(self,state):
        if state:
            if self.velocity[0] < self.maxvelocity:
                self.velocity[0] += 1
        else:
            if self.velocity[0] > 0:
                self.velocity[0] -= 1

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