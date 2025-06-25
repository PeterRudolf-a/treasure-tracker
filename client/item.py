import pygame
import random
import requests
from datetime import datetime, timezone

class Item:
    SPRITE_SIZE = 32
    RARITY_COLORS = {
        "Common": (255, 255, 255),
        "Rare": (0, 0, 255),
        "Legendary": (255, 215, 0)
    }

    def __init__(self, x, y, name, rarity):
        self.sprite = pygame.image.load("assets/item.png").convert_alpha()
        self.sprite = pygame.transform.scale(self.sprite, (self.SPRITE_SIZE, self.SPRITE_SIZE))
        self.rect = pygame.Rect(x, y, self.SPRITE_SIZE, self.SPRITE_SIZE)
        self.name = name
        self.rarity = rarity

    def draw(self, screen, offset):
        screen.blit(self.sprite, (self.rect.x - offset.x, self.rect.y - offset.y))
        pygame.draw.rect(screen, self.RARITY_COLORS[self.rarity], self.rect.move(-offset.x, -offset.y), 2)

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
        x = random.randint(0, 1600 - 32)
        y = random.randint(0, 1200 - 32)
        return Item(x, y, name, rarity)