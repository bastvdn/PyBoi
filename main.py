import pygame
import time
from entity.player import Player
from game.game import Game

pygame.init()

back_color = (80,90,120)
red_color = (255,0,0)
black_color = (0,0,0)
window_resolution = (800,600)


pygame.display.set_caption("PyBoi")
window_surface = pygame.display.set_mode(window_resolution)

clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 5)

arial_font = pygame.font.SysFont("arial",36)
# text = arial_font.render("salut",True,back_color)
# window_surface.blit(text,[50,50])
pygame.display.flip()

print(pygame.time.get_ticks())
game = Game()

launched= True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
        elif event.type == pygame.USEREVENT:
            window_surface.fill(black_color)
            pygame.draw.rect(window_surface, red_color, game.player.hitbox)

            text = arial_font.render(str(game.player.hitbox.x), True, red_color)
            window_surface.blit(text,[50,50])

            pygame.display.flip()


        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

    if game.pressed.get(pygame.K_DOWN):
        game.player.move_down()
    if game.pressed.get(pygame.K_UP):
        game.player.move_up()
    if game.pressed.get(pygame.K_LEFT):
        game.player.move_left()
    if game.pressed.get(pygame.K_RIGHT):
        game.player.move_right()

    
    clock.tick(1)


