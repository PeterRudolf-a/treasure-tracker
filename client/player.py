import pygame

WORLD_WIDTH = 1600
WORLD_HEIGHT = 1200

class Player:
    SPRITE_SIZE = 48

    def __init__(self, x, y):
        sheet = pygame.image.load("assets/player.png").convert_alpha()
        self.image = pygame.transform.scale(sheet, (self.SPRITE_SIZE, self.SPRITE_SIZE))
        self.rect = self.image.get_rect(center=(x, y))

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5

        self.rect.x = max(0, min(self.rect.x, WORLD_WIDTH - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, WORLD_HEIGHT - self.rect.height))

    def draw(self, screen, offset):
        screen.blit(self.image, (self.rect.x - offset.x, self.rect.y - offset.y))