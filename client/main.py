import pygame
import requests
import sys
from menu import show_menu
from game import Game

def register_user(name):
    try:
        response = requests.post("http://localhost:5000/register", json={"name": name})
        response.raise_for_status()
        return response.json()["user_id"]
    except Exception as e:
        print(f"[ERROR] Failed to register user: {e}")
        sys.exit()

def main():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Treasure Tracker")

    name = show_menu(screen)
    user_id = register_user(name)

    clock = pygame.time.Clock()

    while True:
        game = Game(screen, user_id)

        in_game = True
        while in_game:
            while not game.game_over:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()

                game.update()
                game.draw()
                pygame.display.flip()
                clock.tick(60)

            # Game over loop: wait for R or Q
            waiting = True
            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            pygame.quit()
                            sys.exit()
                        elif event.key == pygame.K_r:
                            waiting = False  # exit game over loop
                            in_game = False  # restart outer loop with new Game()
                game.draw()
                pygame.display.flip()
                clock.tick(60)

if __name__ == "__main__":
    main()