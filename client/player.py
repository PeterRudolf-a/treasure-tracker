import pygame

class Player:
    SPRITE_SIZE = 48

    def __init__(self, x, y):
        # You could use subsurface if player.png is a spritesheet
        sheet = pygame.image.load("assets/player.png").convert_alpha()

        # Option A: Use a cropped portion (first tile)
        self.image = sheet.subsurface((0, 0, self.SPRITE_SIZE, self.SPRITE_SIZE))

        # Option B (alternative): scale full image
        # self.image = pygame.transform.scale(sheet, (self.SPRITE_SIZE, self.SPRITE_SIZE))

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
