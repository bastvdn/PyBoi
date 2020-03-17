import pygame
import time
import os
from entity.player import Player

class Ui():
    def __init__(self,player,window):

        self.player = player
        self.window = window

        self.current_path = os.path.dirname("C:/Users/user/Desktop/PyBoi/assets/ui/full_heart.png")

        self.num = {
            '0': 'assets/ui/zero.png',
            '1': 'assets/ui/one.png'
        }
        self.heart = {
            'full_red':'/ui/full_heart.png',
            'half_red':'assets/ui/half_heart.png',
            'empty_red':'assets/ui/empty_heart'
        }


    def show_health(self):
        for n in range(int(self.player.maxhealth/2)):
            image = pygame.image.load("C:/Users/user/Desktop/PyBoi/assets/ui/empty_heart.png")
            image = pygame.transform.scale(image, (30, 30))
            self.window.blit(image,(10+30*n,10))


        for n in range(int(self.player.health/2)):
            if self.player.health%2 and n == int(self.player.health/2):
                image = pygame.image.load("C:/Users/user/Desktop/PyBoi/assets/ui/half_heart.png")
                print("loadhalf")
                
                print(int(self.player.health/2))
            else:
                print("loadfull")
                image = pygame.image.load("C:/Users/user/Desktop/PyBoi/assets/ui/full_heart.png")
            image = pygame.transform.scale(image, (30, 30))
            self.window.blit(image, (10 + 30 * n, 10))

        if self.player.health%2:
            image = pygame.image.load("C:/Users/user/Desktop/PyBoi/assets/ui/full_heart.png")
            image = pygame.transform.scale(image, (30, 30))
            self.window.blit(image, (10 + 30 * n, 10))

