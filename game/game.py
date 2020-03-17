from entity import player
import pygame

class Game():
    def __init__(self):
        self.player = player.Player()
        self.pressed = {}

    def showui(self):
        heart = self.player.maxhealth
        for n in range(heart/2):
            print("ok")
