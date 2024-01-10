import pygame, sys
from button import Button
import imageio
import numpy as np


pygame.init()
SCREEN = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Menu")
gif = imageio.get_reader("jail6x.gif")
frames = [pygame.surfarray.make_surface(np.rot90(frame)) for frame in gif]

def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)


def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        OPTIONS_TEXT = get_font(15).render("This is the OPTIONS screen.", True, "White")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(320, 150))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(320, 260), 
                            text_input="BACK", font=get_font(20), base_color="White", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def menu():
    background_image = pygame.image.load("youwin.jpg")
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(background_image, (0, 0))

        # OPTIONS_TEXT = get_font(15).render("This is the OPTIONS screen.", True, "White")
        # OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(320, 150))
        # SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(320, 350), 
                            text_input="QUIT", font=get_font(20), base_color="White", hovering_color="Blue")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        

def main_menu():
    clock = pygame.time.Clock()
    frame_index = 0
    while True:
        
        SCREEN.blit(frames[frame_index], (0, 0))
        frame_index = (frame_index + 1) % len(frames)
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        clock.tick(7)

        MENU_TEXT = get_font(25).render("Prison        Xcape", True, "#C7FF33")
        MENU_RECT = MENU_TEXT.get_rect(center=(335, 60))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(320, 180), 
                            text_input="PLAY", font=get_font(25), base_color="#FFFFFF", hovering_color="#C7FF33")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(320, 265), 
                            text_input="OPTIONS", font=get_font(25), base_color="#FFFFFF", hovering_color="#C7FF33")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(320, 350), 
                            text_input="QUIT", font=get_font(25), base_color="#FFFFFF", hovering_color="#C7FF33")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    from game import Game
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()