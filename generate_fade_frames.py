import pygame
import os

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
fade_dir = "assets/fade_frames"
os.makedirs(fade_dir, exist_ok=True)

# Generate fade-out frames
for alpha in range(0, 256, 16):  # 0 (fully transparent) to 255 (fully black)
    surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)  # Use alpha channel
    surface.fill((0, 0, 0, alpha))  # RGBA with fading alpha
    filename = os.path.join(fade_dir, f"fade_{alpha:03}.png")
    pygame.image.save(surface, filename)

print("✅ Fade frames successfully created in", fade_dir)

