import pygame,sys
def get_font(size) :
    return pygame.font.SysFont('Comic Sans MS', size, pygame.font.Font.bold)

def Round_Robin():
    pygame.init()
    SCREEN = pygame.display.set_mode((1280, 620))
    pygame.display.set_caption("Round Robin")
    firstp="5"
    stp="3"
    rr="2"
    x=140
    y=320
    a=x-40
    b= d=y+50
    c=x-80
    cir_rect = pygame.rect.Rect(500, 233, x,y)
    cir_rect2 = pygame.rect.Rect(50, 23, a,b)
    cir_rect3 = pygame.rect.Rect(50, 23, c,d)
    rec_list = []
    for i in range(1, 11):
        j=80*i
        rec_list.append(pygame.rect.Rect(200+j, 300, 70, 50))
    while True:
        SCREEN.fill("Black")
        PLAY_TEXT1 = get_font(30).render("THREE processor A B C .", True,"Blue")
        PLAY_RECT1 = PLAY_TEXT1.get_rect(topleft=(0, 0))
        PLAY_TEXT = get_font(45).render("Round Robin Scheduling.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 120))
        SCREEN.blit(PLAY_TEXT1, PLAY_RECT1)
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)
        for i in rec_list :
            pygame.draw.rect(SCREEN, "Blue", i)
        SCREEN.lock()
        cir = pygame.draw.circle(SCREEN, (212, 255, 0), cir_rect.size, 14, 0)
        cir2 = pygame.draw.circle(SCREEN, (212, 255, 0), cir_rect2.size,14, 0)
        cir3 = pygame.draw.circle(SCREEN, (212, 255, 0), cir_rect3.size, 14, 0)
        if cir.colliderect(rec_list[1]):
            y = y + 30
            firstp="4"
        SCREEN.unlock()
        Circle1 = get_font(20).render(firstp, True, "Red")
        Text1 = Circle1.get_rect(center=cir_rect.size)
        SCREEN.blit(Circle1, Text1)
        Circle2 = get_font(20).render(stp, True, "Red")
        Text2 = Circle2.get_rect(center=cir_rect2.size)
        SCREEN.blit(Circle2, Text2)
        Circle3 = get_font(20).render(rr, True, "Red")
        Text3 = Circle3.get_rect(center=cir_rect3.size)
        SCREEN.blit(Circle3, Text3)
        x=x+0.6
        if cir2.collidepoint(355,370) or cir2.collidepoint(595,356):
            b=b-40
        if cir2.colliderect(rec_list[2]):
            b=b+40
            stp="2"
        if cir2.colliderect(rec_list[5]):
            b=b+40
            stp="1"
        if cir2.collidepoint(824,356):
            b=b-40
        if cir2.colliderect(rec_list[8]):
            b=b+40
            stp="0"
        if cir.collidepoint(520,366) or cir.collidepoint(748,366) or cir.collidepoint(910,366):
            y=y-50
        if cir.colliderect(rec_list[4]):
            y=y+50
            firstp="3"
        if cir.colliderect(rec_list[7]):
            y=y+50
            firstp="2"
        if cir.colliderect(rec_list[9]):
            firstp="1"
        if cir3.collidepoint(433,356) or cir3.collidepoint(663,356):
            d=d-50
        if cir3.colliderect(rec_list[3]):
            d=d+50
            rr="1"
        if cir3.colliderect(rec_list[6]):
            d=d+50
            rr="0"
        if cir.collidepoint(1085,316):
            firstp="0"
        print(cir.x ,cir.y)
        a=a+0.6
        c=c+0.6
        cir_rect2.update(0,0,a,b)
        cir_rect.update(0, 0,x,y)
        cir_rect3.update(0,0,c,d)
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                sys.exit()
        pygame.display.update()