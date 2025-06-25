import pygame
from menu import show_menu
from game import Game

def main():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Treasure Tracker")

    name = show_menu(screen)  # returns the entered name
    game = Game(screen, name)

    clock = pygame.time.Clock()
    while True:
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                pygame.quit()
                exit()

        game.update()
        game.draw()
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
