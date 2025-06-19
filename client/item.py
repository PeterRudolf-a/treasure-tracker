import pygame
import random
import requests
from datetime import datetime, timezone

class Item:
    def __init__(self, x, y, name, rarity):
        self.rect = pygame.Rect(x, y, 20, 20)
        self.name = name
        self.rarity = rarity

    def draw(self, screen):
        color = (255, 215, 0) if self.rarity == "Legendary" else (255, 255, 255)
        pygame.draw.rect(screen, color, self.rect)

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
        x, y = random.randint(0, 780), random.randint(0, 580)
        return Item(x, y, name, rarity)
