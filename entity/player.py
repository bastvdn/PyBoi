import pygame
import math
from projectiles.tear import Tear

class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.health = 6
        self.maxhealth = 6
        self.velocity = [0,0]
        self.maxvelocity = 10
        self.damages = 10
        #self.hitbox = pygame.Rect(10,10,50,50).
        self.image = pygame.image.load('assets/isaac.png')
        self.image = pygame.transform.scale(self.image,(100,120))
        self.hitbox = self.image.get_rect()
        self.all_projectiles = pygame.sprite.Group()
        self.tear_cd = 300
        self.temp = pygame.time.get_ticks()
        self.range = 600

    def position(self):
        """
        Repositionne le koueur à chaque tick en fonction de sa vélocité actuelle

        :return:
        """


        if self.get_speed() >= self.maxvelocity:       #coeficient qui gère les diagonnales pour faire en sorte qu'on ne dépasse pas la v max
            coef = self.get_speed()/self.maxvelocity
        else:
            coef = 1

        if self.hitbox.x > 10 and self.hitbox.x < 1200:        #si on est dans la zone de jeu
            self.hitbox.x += int(self.velocity[0]/coef)         #on déplace le joueur
            if -self.maxvelocity/20 < self.velocity[0] < self.maxvelocity/20:
                self.velocity[0] = 0
        else:
            if self.hitbox.x < 500:                             #si il n'est pas dans la zone de jeu on le téléporte au bord avec une vitesse nulle
                self.hitbox.x = 11
                self.velocity[0] = 0
            if self.hitbox.x > 500:
                self.hitbox.x = 1199
                self.velocity[0] = 0

        if self.hitbox.y > 10 and self.hitbox.y < 640:
            self.hitbox.y += int(self.velocity[1]/coef)
            if -self.maxvelocity/20 < self.velocity[1] < self.maxvelocity/20:
                self.velocity[1] = 0
        else:
            if self.hitbox.y < 500:
                self.hitbox.y = 11
                self.velocity[1] = 0
            if self.hitbox.y > 500:
                self.hitbox.y = 639
                self.velocity[1] = 0


    def shoot(self,direction):
        """
        creates a tear that will be launched in the wanted direction
        :param direction: 0 right, 1 up, 2 left, 3 down
        :return:
        """
        if (pygame.time.get_ticks()-self.temp)>self.tear_cd:  #if the last tear was launched since more than the tear cd
            self.all_projectiles.add(Tear(self,direction))
            self.temp = pygame.time.get_ticks()
        else:
            pass


    def get_speed(self):
        """
        get the absolute speed back (x and y combined)
        :return: the speed vector norm
        """

        return math.sqrt((self.velocity[0]**2)+(self.velocity[1]**2))

    def move_right(self,state):
        """
        changes the current velocity
        :param state: the button is pressed or not
        :return:
        """
        if state:                                                                       #if its pressed
            if -self.maxvelocity/4 < int(self.velocity[0]) < self.maxvelocity / 2:      #if the speed is low enough
                self.velocity[0] = self.maxvelocity / 2                                 #it goes to half of the max speed
            if self.velocity[0] < self.maxvelocity:
                self.velocity[0] += self.maxvelocity/30                                 #it increase by 1/30 every tick
        else:
            if self.velocity[0] > 0:                                                    #if the button isnt pressed
                self.velocity[0] -= self.maxvelocity/20                                 #the speed decreases 1/20 every tick

    def move_left(self,state):
        if state:
            if self.maxvelocity/4 > int(self.velocity[0]) > -self.maxvelocity / 2:
                self.velocity[0] = -self.maxvelocity / 2
            if self.velocity[0] > -self.maxvelocity:
                self.velocity[0] -= self.maxvelocity/30
        else:
            if self.velocity[0] < 0:
                self.velocity[0] +=self.maxvelocity/20

    def move_up(self,state):
        if state:
            if self.maxvelocity/4 > int(self.velocity[1]) > -self.maxvelocity / 2:
                self.velocity[1] = -self.maxvelocity / 2

            if self.velocity[1] > -self.maxvelocity:
                self.velocity[1] -= self.maxvelocity/30
        else:
            if self.velocity[1] < 0:
                self.velocity[1] += self.maxvelocity/20

    def move_down(self,state):
        if state:
            if -self.maxvelocity/4 < int(self.velocity[1]) < self.maxvelocity / 2:
                self.velocity[1] = self.maxvelocity / 2
            if self.velocity[1] < self.maxvelocity:
                self.velocity[1] += self.maxvelocity/30
        else:
            if self.velocity[1] > 0:
                self.velocity[1] -= self.maxvelocity/20