import pygame
import time
from entity.player import Player
from game.ui import Ui
from projectiles.tear import Tear


class Game():
    def __init__(self):
        self.player = Player()
        self.pressed = {}

        self.window_resolution = (1280, 720)

        self.back_color = (80, 90, 120)
        self.red_color = (255, 0, 0)
        self.black_color = (165, 42, 42)

        pygame.init()
        pygame.display.set_caption("PyBoi")
        self.window_surface = pygame.display.set_mode(self.window_resolution)

        #textures UI
        self.ui = Ui(self.player,self.window_surface)


        # mise en place des timers
        self.clock = pygame.time.Clock()
        pygame.time.set_timer(pygame.USEREVENT,3)
        self.stop = 0
        self.i = 0

        # mise en place font
        self.arial_font = pygame.font.SysFont("arial", 30)

    def showui(self):
        self.ui.show_health()

    def start_game(self):
        launched = True
        text_timer = self.arial_font.render("", True, self.red_color)
        while launched:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    launched = False
                elif event.type == pygame.USEREVENT:
                    self.window_surface.fill(self.back_color)
                    self.window_surface.blit(self.player.image, (self.player.hitbox.x, self.player.hitbox.y))

                    self.player.all_projectiles.draw(self.window_surface)

                    # infos vélo
                    text_velo = self.arial_font.render(
                        str(int(self.player.velocity[0])) + "," + str(int(self.player.velocity[1])), True, self.red_color)
                    self.window_surface.blit(text_velo, [1000, 50])

                    # info timer
                    timer_list = []
                    if self.stop != 0:
                        text_timer = self.arial_font.render(str(stop) + " ticks", True, self.red_color)
                        timer_list.append(text_timer)
                        stop = 0
                    self.window_surface.blit(text_timer, [1000, 150])

                    # infos FPS
                    text = self.arial_font.render(str(int(self.clock.get_fps())) + " FPS", True, self.red_color)
                    self.window_surface.blit(text, [1000, 100])

                    pygame.draw.line(self.window_surface, self.red_color, (self.player.hitbox.x + 50, self.player.hitbox.y + 60),
                                     (self.player.hitbox.x + 50 + 20 * self.player.velocity[0],
                                      self.player.hitbox.y + 60 + 20 * self.player.velocity[1]), 5)
                    self.showui()
                    pygame.display.flip()


                elif event.type == pygame.KEYDOWN:
                    stop = 0
                    start = pygame.time.get_ticks()
                    self.pressed[event.key] = True

                elif event.type == pygame.KEYUP:
                    stop = pygame.time.get_ticks() - start

                    self.pressed[event.key] = False

            if self.pressed.get(pygame.K_d):
                self.player.move_down(True)
            else:
                self.player.move_down(False)

            if self.pressed.get(pygame.K_e):
                self.player.move_up(True)
            else:
                self.player.move_up(False)

            if self.pressed.get(pygame.K_s):
                self.player.move_left(True)
            else:
                self.player.move_left(False)

            if self.pressed.get(pygame.K_f):
                self.player.move_right(True)
            else:
                self.player.move_right(False)

            if self.pressed.get(pygame.K_DOWN):
                self.player.shoot(3)
            if self.pressed.get(pygame.K_UP):
                self.player.shoot(1)
            if self.pressed.get(pygame.K_RIGHT):
                self.player.shoot(0)
            if self.pressed.get(pygame.K_LEFT):
                self.player.shoot(2)

            self.player.position()
            for tears in self.player.all_projectiles:
                tears.move()

            self.clock.tick(60)

game = Game()
game.start_game()

