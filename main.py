import pygame, sys
from pygame import *
from button import Button

pygame.init()

SCREEN_SIZE = pygame.Rect((0, 0, 800, 640))
SCREEN = pygame.display.set_mode(SCREEN_SIZE.size)
pygame.display.set_caption("Menu")

TILE_SIZE = 32 
GRAVITY = pygame.Vector2((0, 0.3))
LEVEL_NUM = 1
LEVEL_VER = 1

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def play(): # Play Screen
    pygame.display.set_caption("Play")

    while True:
        SCREEN.fill("black")
        
        PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

def leader(): # Leaderboard Screen
    pygame.display.set_caption("Leaderboard")

    while True:
        SCREEN.fill("black")
        
        LEADER_TEXT = get_font(45).render("This is the LEADERBOARD.", True, "White")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


def main_menu(): # Main Menu Screen
    pygame.display.set_caption("Menu")

    while True:
        SCREEN.fill("black")

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(75).render("MAIN MENU", True, "White")
        MENU_RECT = MENU_TEXT.get_rect(center=(400, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(400, 250), 
                            text_input="PLAY", font=get_font(50), base_col="#d7fcd4", hovering_col="Orange")
        LEADER_BUTTON = Button(image=pygame.image.load("assets/Leaderboard Rect.png"), pos=(400, 400), 
                            text_input="LEADERBOARD", font=get_font(50), base_col="#d7fcd4", hovering_col="Orange")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(400, 550), 
                            text_input="QUIT", font=get_font(50), base_col="#d7fcd4", hovering_col="Orange")
        
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, LEADER_BUTTON, QUIT_BUTTON]:
            button.changeColour(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if LEADER_BUTTON.checkForInput(MENU_MOUSE_POS):
                    leader()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()