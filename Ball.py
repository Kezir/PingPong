import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Ball(pygame.sprite.Sprite):
    def __init__(self,color):
        super().__init__()
        self.image = pygame.Surface([10,10])
        self.image.fill(WHITE)
        pygame.draw.circle(self.image,color,(10,10),10)
        self.rect = self.image.get_rect()
        self.speedx = 4
        self.speedy = 4

    def move(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy