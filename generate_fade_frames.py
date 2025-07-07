import pygame
import os

pygame.init()

# Create directory to store frames
fade_dir = "assets/fade_frames"
os.makedirs(fade_dir, exist_ok=True)

# Create fade-out frames from transparent to black
for alpha in range(0, 256, 16):  # 0 to 255 by steps of 16
    surface = pygame.Surface((800, 600))  # Match your game resolution
    surface.fill((0, 0, 0))
    surface.set_alpha(alpha)
    pygame.image.save(surface, f"{fade_dir}/fade_{alpha:03}.png")

print("✅ Fade frames generated in:", fade_dir)
