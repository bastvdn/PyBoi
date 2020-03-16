import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.health = 6
        self.maxhealth = 6
        self.velocity = 0
        self.maxvelocity = 15
        self.damages = 10
        self.hitbox = pygame.Rect(10,10,50,50)


    def position(self,axe):

        self.hitbox.x += self.velocity

    def move_right(self):

        if self.velocity < self.maxvelocity:
            self.velocity += 1
            self.position("x")
        elif self.velocity == self.maxvelocity:
            self.position("x")
            print("vmax")

    def move_left(self):
        self.hitbox.x -= self.velocity

    def move_up(self):
        self.hitbox.y -= self.velocity

    def move_down(self):
        self.hitbox.y += self.velocity