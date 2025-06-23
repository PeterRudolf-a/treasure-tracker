import pygame
import random
import requests
from datetime import datetime, timezone

class Item:
    SPRITE_SIZE = 32  # Class-level constant

    def __init__(self, x, y, name, rarity):
        self.sprite = pygame.image.load("assets/item.png").convert_alpha()
        self.rect = pygame.Rect(x, y, self.SPRITE_SIZE, self.SPRITE_SIZE)
        self.name = name
        self.rarity = rarity

    def draw(self, screen):
        screen.blit(self.sprite, self.rect)

    def send_to_server(self, user_id):
        data = {
            "user_id": user_id,
            "item_name": self.name,
            "rarity": self.rarity,
            "collected_at": datetime.now(timezone.utc).isoformat(),
        }
        try:
            requests.post("http://localhost:5000/collect", json=data)
        except Exception as e:
            print(f"Failed to send item to server: {e}")

    @staticmethod
    def random_spawn():
        name = random.choice(["Ruby", "Emerald", "Golden Idol"])
        rarity = random.choice(["Common", "Rare", "Legendary"])
        x, y = random.randint(0, 768), random.randint(0, 568)
        return Item(x, y, name, rarity)

