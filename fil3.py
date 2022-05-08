import pygame,sys
def get_font(size) :
    return pygame.font.SysFont('Comic Sans MS', size, pygame.font.Font.bold)
def third():
    pygame.init()
    SCREEN = pygame.display.set_mode((1280, 620))
    pygame.display.set_caption("Menu")
    SCREEN.fill("Black")
    x=30
    y=320
    cir_rect = pygame.rect.Rect(500, 233, x, y)
    cir_rect2 = pygame.rect.Rect(50, 23, x,y)
    cir_rect3 = pygame.rect.Rect(50, 23, x,y)
    cir_list = []
    for i in range(1, 11) :
        j=80*i
        cir_list.append(pygame.rect.Rect(200+j, 300, 70, 50))
    while True:
        PLAY_TEXT1 = get_font(30).render("THREE processor A B C .", True,"Blue")
        PLAY_RECT1 = PLAY_TEXT1.get_rect(topleft=(0, 0))
        PLAY_TEXT = get_font(45).render("Round Robin Scheduling.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 120))
        SCREEN.blit(PLAY_TEXT1, PLAY_RECT1)
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)
        for i in cir_list:
            pygame.draw.rect(SCREEN, "Blue", i)
        SCREEN.lock()
        cir = pygame.draw.circle(SCREEN, (212, 255, 0), cir_rect2.size, 15, 0)
        if cir.collidepoint(350, 300):
            y = y + 24
        SCREEN.unlock()
        x=x+1
        cir_rect2.update(0, 0, x, y)








        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                pygame.display.flip()
        pygame.display.update()
third()