import pygame
import requests
from game import Game

# Prompt user to enter name in-game
def prompt_for_name(screen):
    font = pygame.font.Font(None, 48)
    input_box = pygame.Rect(250, 250, 300, 50)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = True
                else:
                    active = False
                color = color_active if active else color_inactive
            elif event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        if text.strip() != "":
                            done = True
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill((30, 30, 30))
        txt_surface = font.render(text, True, color)
        input_box.w = max(300, txt_surface.get_width() + 10)
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, color, input_box, 2)

        instruction = font.render("Enter your name:", True, pygame.Color('white'))
        screen.blit(instruction, (250, 200))

        pygame.display.flip()

    return text

# Game entry point
def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Treasure Tracker")
    clock = pygame.time.Clock()

    # Prompt for player name via Pygame UI
    name = prompt_for_name(screen)

    # Register player with Flask API
    try:
        res = requests.post("http://localhost:5000/register", json={"name": name})
        user_id = res.json().get("user_id")
        print(f"User ID received: {user_id}")
    except Exception as e:
        print(f"Failed to register user: {e}")
        pygame.quit()
        return

    # Start game
    game = Game(screen, user_id)
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        game.update()
        game.draw()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
