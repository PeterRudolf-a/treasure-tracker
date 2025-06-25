import pygame

def show_menu(screen):
    font_title = pygame.font.SysFont("Arial", 48)
    font_input = pygame.font.SysFont("Arial", 32)
    title = font_title.render("Treasure Tracker", True, (255, 255, 255))
    instruction = font_input.render("Enter your name and press Enter:", True, (200, 200, 200))

    input_box = pygame.Rect(200, 250, 400, 50)
    active, text = False, ""

    clock = pygame.time.Clock()
    while True:
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif evt.type == pygame.MOUSEBUTTONDOWN:
                active = input_box.collidepoint(evt.pos)
            elif evt.type == pygame.KEYDOWN and active:
                if evt.key == pygame.K_RETURN and text.strip():
                    return text.strip()
                elif evt.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += evt.unicode

        screen.fill((0, 0, 0))
        screen.blit(title, (200, 100))
        screen.blit(instruction, (200, 200))

        pygame.draw.rect(screen, (100, 100, 100), input_box, 2)
        txt_surf = font_input.render(text, True, (255, 255, 255))
        screen.blit(txt_surf, (input_box.x + 5, input_box.y + 5))
        input_box.w = max(400, txt_surf.get_width() + 10)

        pygame.display.flip()
        clock.tick(30)
