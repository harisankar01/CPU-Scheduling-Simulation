import pygame,sys
def get_font(size) :  # Returns Press-Start-2P in the desired size
    return pygame.font.SysFont('Comic Sans MS', size, pygame.font.Font.bold)
def third():
    pygame.init()
    SCREEN = pygame.display.set_mode((1280, 620))
    pygame.display.set_caption("Menu")
