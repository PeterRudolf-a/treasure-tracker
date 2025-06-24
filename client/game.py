import pygame
from player import Player
from item import Item

class Game:
    def __init__(self, screen, user_id):
        self.screen = screen
        self.user_id = user_id
        self.player = Player(400, 300)
        self.items = [Item.random_spawn() for _ in range(5)]
        self.score = 0

        self.bg_tile = pygame.image.load("assets/background.png").convert()
        self.font = pygame.font.SysFont("Arial", 24)

        # Load sound effect
        try:
            self.collect_sound = pygame.mixer.Sound("assets/collect.wav")
        except:
            self.collect_sound = None

    def update(self):
        keys = pygame.key.get_pressed()
        self.player.move(keys)

        if keys[pygame.K_q]:
            pygame.quit()
            exit()

        for item in self.items[:]:
            if self.player.rect.colliderect(item.rect):
                item.send_to_server(self.user_id)
                self.items.remove(item)
                self.score += 1
                if self.collect_sound:
                    self.collect_sound.play()

    def draw(self):
        # Draw tiled background
        tile_w, tile_h = self.bg_tile.get_size()
        for x in range(0, 800, tile_w):
            for y in range(0, 600, tile_h):
                self.screen.blit(self.bg_tile, (x, y))

        self.player.draw(self.screen)
        for item in self.items:
            item.draw(self.screen)

        # Draw score
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))

        # Draw quit instruction
        quit_text = self.font.render("Press Q to Quit", True, (200, 200, 200))
        self.screen.blit(quit_text, (10, 40))
