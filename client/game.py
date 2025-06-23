from player import Player
from item import Item
import pygame

class Game:
    def __init__(self, screen, user_id):
        self.screen = screen
        self.user_id = user_id
        self.player = Player(400, 300)
        self.items = [Item.random_spawn() for _ in range(5)]

        # Load background tile (optional)
        try:
            self.bg_tile = pygame.image.load("assets/background.png").convert()
        except:
            self.bg_tile = None

    def update(self):
        keys = pygame.key.get_pressed()
        self.player.move(keys)

        for item in self.items[:]:
            if self.player.rect.colliderect(item.rect):
                item.send_to_server(self.user_id)
                self.items.remove(item)

    def draw(self):
        if self.bg_tile:
            # Tile the background
            tile_w, tile_h = self.bg_tile.get_size()
            for x in range(0, 800, tile_w):
                for y in range(0, 600, tile_h):
                    self.screen.blit(self.bg_tile, (x, y))
        else:
            self.screen.fill((30, 30, 30))  # fallback color

        self.player.draw(self.screen)
        for item in self.items:
            item.draw(self.screen)
