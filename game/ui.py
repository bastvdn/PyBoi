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
            '1': 'assets/ui/one.png',
            '2': 'assets/ui/two.png',
            '3': 'assets/ui/three.png',
            '4': 'assets/ui/four.png',
            '5': 'assets/ui/five.png',
            '6': 'assets/ui/six.png',
            '7': 'assets/ui/seven.png',
            '8': 'assets/ui/eight.png',
            '9': 'assets/ui/nine.png'

        }
        self.heart = {
            'full_red':'assets/ui/full_heart.png',
            'half_red':'assets/ui/half_heart.png',
            'empty_red':'assets/ui/empty_heart.png'
        }
        self.cons = {
            'coin':'assets/ui/coin.png',
            'bomb':'assets/ui/bomb.png',
            'key': 'assets/ui/key.png'
        }


    def show_health(self):
        for n in range(int(self.player.maxhealth/2)):
            image = pygame.image.load(self.heart['empty_red'])
            image = pygame.transform.scale(image, (30, 30))
            self.window.blit(image,(10+30*n,10))


        for n in range(int(self.player.health/2)+1):
            if self.player.health%2 == 1 and n == int(self.player.health/2):
                image = pygame.image.load(self.heart['half_red'])
            else:
                image = pygame.image.load(self.heart['full_red'])
            image = pygame.transform.scale(image, (30, 30))
            self.window.blit(image, (10 + 30 * n, 10))

    def show_bombs_key_coin(self):
        if len(str(self.player.coin)) == 1:
            image0 = pygame.image.load(self.num['0'])
            image0 = pygame.transform.scale(image0, (15, 15))
            image1 = pygame.image.load(self.num[str(self.player.coin)])
            image1 = pygame.transform.scale(image1, (15, 15))
        else:
            image0 = pygame.image.load(self.num[str(self.player.coin)[0]])
            image0 = pygame.transform.scale(image0, (15, 15))
            image1 = pygame.image.load(self.num[str(self.player.coin)[1]])
            image1 = pygame.transform.scale(image1, (15, 15))
        self.window.blit(image0, (35 ,60))
        self.window.blit(image1, (50, 60))
        coinimg =  pygame.image.load(self.cons['coin'])
        coinimg = pygame.transform.scale(coinimg, (30, 30))
        self.window.blit(coinimg, (5, 50))


        if len(str(self.player.bombs)) == 1:
            bombs0 = pygame.image.load(self.num['0'])
            bombs0 = pygame.transform.scale(bombs0, (15, 15))
            bombs1 = pygame.image.load(self.num[str(self.player.bombs)])
            bombs1 = pygame.transform.scale(bombs1, (15, 15))
        else:
            bombs0 = pygame.image.load(self.num[str(self.player.bombs)[0]])
            bombs0 = pygame.transform.scale(bombs0, (15, 15))
            bombs1 = pygame.image.load(self.num[str(self.player.bombs)[1]])
            bombs1 = pygame.transform.scale(bombs1, (15, 15))
        self.window.blit(bombs0, (35, 95))
        self.window.blit(bombs1, (50, 95))
        bombimg = pygame.image.load(self.cons['bomb'])
        bombimg = pygame.transform.scale(bombimg, (30, 30))
        self.window.blit(bombimg, (5, 85))

        if len(str(self.player.key)) == 1:
            key0 = pygame.image.load(self.num['0'])
            key0 = pygame.transform.scale(key0, (15, 15))
            key1 = pygame.image.load(self.num[str(self.player.key)])
            key1 = pygame.transform.scale(key1, (15, 15))
        else:
            key0 = pygame.image.load(self.num[str(self.player.key)[0]])
            key0 = pygame.transform.scale(key0, (15, 15))
            key1 = pygame.image.load(self.num[str(self.player.key)[1]])
            key1 = pygame.transform.scale(key1, (15, 15))
        self.window.blit(key0, (35, 135))
        self.window.blit(key1, (50, 135))
        keyimg = pygame.image.load(self.cons['key'])
        keyimg = pygame.transform.scale(keyimg, (25, 35))
        self.window.blit(keyimg, (5, 125))


