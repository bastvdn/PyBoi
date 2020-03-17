import pygame
import time
from entity.player import Player
from game.game import Game
from projectiles.tear import Tear

pygame.init()

back_color = (80,90,120)
red_color = (255,0,0)
black_color = (165,42,42)
window_resolution = (1280,720)

#mise en place fenetre
pygame.display.set_caption("PyBoi")
window_surface = pygame.display.set_mode(window_resolution)

#mise en place des timers
clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 1)
stop = 0
i=0

#mise en place font
arial_font = pygame.font.SysFont("arial",30)

pygame.display.flip()

game = Game()
text_timer = arial_font.render(str(stop) + " ticks", True, red_color)

launched= True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
        elif event.type == pygame.USEREVENT:
            window_surface.fill(back_color)
            window_surface.blit(game.player.image, (game.player.hitbox.x,game.player.hitbox.y))

            game.player.all_projectiles.draw(window_surface)

            #infos vélo
            text_velo = arial_font.render(str(int(game.player.velocity[0]))+","+str(int(game.player.velocity[1])), True, red_color)
            window_surface.blit(text_velo,[1000,50])

            # info timer
            timer_list = []
            if stop != 0:
                text_timer = arial_font.render(str(stop) + " ticks", True, red_color)
                timer_list.append(text_timer)
                stop=0
            window_surface.blit(text_timer, [1000, 150])

            #infos FPS
            text = arial_font.render(str(int(clock.get_fps()))+" FPS", True, red_color)
            window_surface.blit(text, [1000,100])

            pygame.draw.line(window_surface,red_color,(game.player.hitbox.x+50,game.player.hitbox.y+60),(game.player.hitbox.x+50+20*game.player.velocity[0],game.player.hitbox.y+60+20*game.player.velocity[1]),5)

            pygame.display.flip()


        elif event.type == pygame.KEYDOWN:
            stop = 0
            start = pygame.time.get_ticks()
            game.pressed[event.key] = True

        elif event.type == pygame.KEYUP:
            stop = pygame.time.get_ticks() - start

            game.pressed[event.key] = False

    if game.pressed.get(pygame.K_d):
        game.player.move_down(True)
    else:
        game.player.move_down(False)

    if game.pressed.get(pygame.K_e):
        game.player.move_up(True)
    else:
        game.player.move_up(False)

    if game.pressed.get(pygame.K_s):
        game.player.move_left(True)
    else:
        game.player.move_left(False)

    if game.pressed.get(pygame.K_f):
        game.player.move_right(True)
    else:
        game.player.move_right(False)

    if game.pressed.get(pygame.K_DOWN):
        game.player.shoot(3)
    if game.pressed.get(pygame.K_UP):
        game.player.shoot(1)
    if game.pressed.get(pygame.K_RIGHT):
        game.player.shoot(0)
    if game.pressed.get(pygame.K_LEFT):
        game.player.shoot(2)


    game.player.position()
    for tears in game.player.all_projectiles:
        tears.move()

    clock.tick(60)


