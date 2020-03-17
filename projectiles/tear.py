import pygame

class Tear(pygame.sprite.Sprite):

    def __init__(self,player,direction):
        super().__init__()
        self.velocity = 15
        self.image = pygame.image.load('assets/tear.png')
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.player = player
        self.rect = self.image.get_rect()
        self.rect.move_ip(player.hitbox.x+50,player.hitbox.y+40)
        self.initial_momentum = (player.velocity[0],player.velocity[1])
        self.direction = direction
        self.current_range = 0

    def remove_tear(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        if 0 < self.rect.x < 1300 and 0 < self.rect.y <750 and self.current_range < self.player.range:
            if self.direction == 0:
                if self.initial_momentum[0] > 0:
                    self.rect.x += self.velocity + self.initial_momentum[0]
                else:
                    self.rect.x += self.velocity
                self.current_range += self.velocity
                self.rect.y += self.initial_momentum[1]/2

            elif self.direction == 1:
                if self.initial_momentum[1] < 0:
                    self.rect.y -= (self.velocity - self.initial_momentum[1])
                else:
                    self.rect.y -= self.velocity
                self.current_range += self.velocity
                self.rect.x += self.initial_momentum[0]/2

            elif self.direction == 2:
                self.rect.x -= self.velocity
            elif self.direction == 3:
                self.rect.y += self.velocity
        else:
            self.remove_tear()