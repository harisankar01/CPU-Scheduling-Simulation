import pygame, sys
import RoundRobin
def get_font(size) :
    return pygame.font.SysFont('Comic Sans MS', size, pygame.font.Font.bold)


def SJF() :
    sc3 = False
    pygame.init()
    SCREEN = pygame.display.set_mode((1280, 620))
    pygame.display.set_caption("Menu")
    val1=20
    val2=15
    val3=8
    val4=12
    x = e = 300
    y = 320
    a = x - 100
    b = d = f = y + 55
    c = x - 200
    hit2, hit3, hitFlag, flag, flag2, flag3 = (False,) * 6
    cir_rect = pygame.rect.Rect(500, 233, x, y)
    cir_rect2 = pygame.rect.Rect(500, 233, e, f)
    cir_rect3 = pygame.rect.Rect(500, 233, a, b)
    cir_rect4 = pygame.rect.Rect(500, 233, c, d)
    rex = pygame.rect.Rect(700, 300, 120, 50)
    dex = pygame.rect.Rect(822, 300, 120, 50)
    gex = pygame.rect.Rect(944, 300, 120, 50)
    pix = pygame.rect.Rect(1066, 300, 120, 50)
    oox = pygame.rect.Rect(1188, 300, 120, 50)
    while True :
        SCREEN.fill("Black")
        PLAY_TEXT1 = get_font(30).render("Four processor A at 0 min | B at 1 min | C at 2 min |  D at 3 min.", True,
                                         "Blue")
        PLAY_RECT1 = PLAY_TEXT1.get_rect(topleft=(0, 0))
        PLAY_TEXT = get_font(45).render("SJF Scheduling.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 120))
        SCREEN.blit(PLAY_TEXT1, PLAY_RECT1)
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)
        pygame.draw.rect(SCREEN, "Blue", rex)
        pygame.draw.rect(SCREEN, "Blue", dex)
        pygame.draw.rect(SCREEN, "Blue", gex)
        pygame.draw.rect(SCREEN, "Blue", pix)
        SCREEN.lock()
        cir = pygame.draw.circle(SCREEN, (212, 255, 0), cir_rect.size, 20, 0)
        if flag :
            cir2 = pygame.draw.circle(SCREEN, (212, 255, 0), cir_rect2.size, 20, 0)
            if cir2.colliderect(oox) :
                f = f + 1
                val2=0
        if flag2 :
            cir3 = pygame.draw.circle(SCREEN, (212, 255, 0), cir_rect3.size, 20, 0)
            if cir3.colliderect(gex) :
                b = b + 1
                hit2 = True
                val3=0
        if flag3 :
            cir4 = pygame.draw.circle(SCREEN, (212, 255, 0), cir_rect4.size, 20, 0)
            if cir4.colliderect(pix) :
                d = d + 1
                hit3 = True
                val4=0
        SCREEN.unlock()
        if hitFlag :
            a = a + 1
            if 800 > a > 795 :
                b = b - 13
        if hit2 :
            c = c + 1
            if 920 > c > 915 :
                d = d - 13
        if hit3 :
            e = e + 1
            if 1040 > e > 1035 :
                f = f - 13
            if e > 1200 :
                sc3 = True
                RoundRobin.Round_Robin()

        Cir_TEXT = get_font(18).render(str(val1), True, "Red")
        Cir_RECT = Cir_TEXT.get_rect(center=cir_rect.size)
        SCREEN.blit(Cir_TEXT, Cir_RECT)
        if flag :
            Cir_TEXT2 = get_font(18).render(str(val2), True, "Red")
            Cir_RECT2 = Cir_TEXT2.get_rect(center=cir_rect2.size)
            SCREEN.blit(Cir_TEXT2, Cir_RECT2)
        if flag2 :
            Cir_TEXT3 = get_font(18).render(str(val3), True, "Red")
            Cir_RECT3 = Cir_TEXT3.get_rect(center=cir_rect3.size)
            SCREEN.blit(Cir_TEXT3, Cir_RECT3)
        if flag3 :
            Cir_TEXT4 = get_font(18).render(str(val4), True, "Red")
            Cir_RECT4 = Cir_TEXT4.get_rect(center=cir_rect4.size)
            SCREEN.blit(Cir_TEXT4, Cir_RECT4)
        x = x + 1
        cir_rect.update(0, 0, x, y)
        cir_rect3.update(0, 0, a, b)
        cir_rect4.update(0, 0, c, d)
        cir_rect2.update(0, 0, e, f)
        if cir.collidepoint(755, 300) :
            flag = True
        if cir.collidepoint(775, 300) :
            flag2 = True
        if cir.collidepoint(800, 300) :
            flag3 = True
        if cir.colliderect(dex) :
            y = y + 1
            hitFlag = True
            val1=0

        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                sys.exit()
        pygame.display.update()