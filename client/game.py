from player import Player
from item import Item
import pygame

class Game:
    def __init__(self, screen, user_id):
        self.screen = screen
        self.user_id = user_id  # Store the user ID for server communication
        self.player = Player(400, 300)
        self.items = [Item.random_spawn() for _ in range(5)]

    def update(self):
        keys = pygame.key.get_pressed()
        self.player.move(keys)
        for item in self.items[:]:
            if self.player.rect.colliderect(item.rect):
                # Use the user_id passed to the Game class when sending to the server
                item.send_to_server(self.user_id)  # Use dynamic user ID

    def draw(self):
        self.screen.fill((30, 30, 30))
        self.player.draw(self.screen)
        for item in self.items:
            item.draw(self.screen)
