import pygame
from player import Player
from item import Item
import sys
import os

# Add the server directory to the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "server")))
from models import save_score

TILE_SIZE = 64
WORLD_WIDTH = 1600
WORLD_HEIGHT = 1200

class Game:
    def __init__(self, screen, user_id):
        self.screen = screen
        self.user_id = user_id
        self.player = Player(400, 300)
        self.items = []
        self.generate_items(30)
        self.score = 0

        self.bg_tile = pygame.image.load("assets/background.png").convert()
        self.font = pygame.font.SysFont("Arial", 24)
        self.collect_sound = pygame.mixer.Sound("assets/collect.wav")

        self.start_time = pygame.time.get_ticks()
        self.time_limit = 60000  # 60 seconds
        self.game_over = False
        self.play_again = False  # Flag to trigger restart from main.py
        self.fade_frames = [
            pygame.image.load(f"assets/fade_frames/fade_{alpha:03}.png").convert_alpha()
            for alpha in range(0, 256, 16)
        ]

    def fade_out(self):
        for frame in self.fade_frames:
            self.draw()  # Redraw everything underneath
            self.screen.blit(frame, (0, 0))  # Overlay the fade frame
            pygame.display.flip()
            pygame.time.delay(40)  # Delay between frames (adjust for speed)



    def generate_items(self, count):
        for _ in range(count):
            self.items.append(Item.random_spawn())

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif self.game_over:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.play_again = True
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()

        if self.game_over:
            return

        keys = pygame.key.get_pressed()
        self.player.move(keys)

        for item in self.items[:]:
            if self.player.rect.colliderect(item.rect.inflate(-10, -10)):
                item.send_to_server(self.user_id)
                self.items.remove(item)
                self.score += {"Common": 1, "Rare": 3, "Legendary": 5}[item.rarity]
                self.collect_sound.play()

        remaining = max(0, (self.time_limit - (pygame.time.get_ticks() - self.start_time)))
        if remaining == 0 and not self.game_over:
            self.game_over = True
            save_score(self.user_id, self.score)
            self.fade_out()
            


    def draw(self):
        offset = pygame.Vector2(self.player.rect.centerx - 400, self.player.rect.centery - 300)

        screen_width, screen_height = self.screen.get_size()
        for x in range(int(offset.x // TILE_SIZE) * TILE_SIZE, int(offset.x + screen_width), TILE_SIZE):
            for y in range(int(offset.y // TILE_SIZE) * TILE_SIZE, int(offset.y + screen_height), TILE_SIZE):
                self.screen.blit(self.bg_tile, (x - offset.x, y - offset.y))

        for item in self.items:
            item.draw(self.screen, offset)
        self.player.draw(self.screen, offset)

        # Score and timer HUD
        pygame.draw.rect(self.screen, (0, 0, 0), (5, 5, 160, 30))
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))

        remaining = max(0, (self.time_limit - (pygame.time.get_ticks() - self.start_time)) // 1000)
        timer_text = self.font.render(f"Time: {remaining}", True, (255, 255, 255))
        self.screen.blit(timer_text, (680, 10))

        if self.game_over:
            end_text = self.font.render("⏰ Time's up!", True, (255, 0, 0))
            prompt_text = self.font.render("Press R to Play Again or Q to Quit", True, (255, 255, 255))
            self.screen.blit(end_text, (270, 280))
            self.screen.blit(prompt_text, (170, 320))
