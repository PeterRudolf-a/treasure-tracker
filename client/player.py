import pygame

class Player:
    SPRITE_SIZE = 48

    def __init__(self, x, y):
        sheet = pygame.image.load("assets/player.png").convert_alpha()
        self.image = pygame.transform.scale(sheet, (48, 48))

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

    def draw(self, screen):
        screen.blit(self.image, self.rect)
