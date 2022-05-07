import pygame,sys
pygame.init()
global cirl
SCREEN = pygame.display.set_mode((1280, 620))
pygame.display.set_caption("Menu")
x=300
y=320
z=x
c=370
flag=False
circle_list=[]
cir_rect=pygame.rect.Rect(500,233,x,y)
cir_rect2=pygame.rect.Rect(500,233,x,y)
rex=pygame.rect.Rect(700, 300, 120, 50)
dex=pygame.rect.Rect(822, 300, 120, 50)
gex=pygame.rect.Rect(944, 300, 120, 50)
pix=pygame.rect.Rect(1046, 300, 80, 50)
collist=[rex,dex,gex,pix]
def get_font(size) :  # Returns Press-Start-2P in the desired size
    return pygame.font.SysFont('Comic Sans MS', size, pygame.font.Font.bold)

while True :
    PLAY_MOUSE_POS = pygame.mouse.get_pos()

    SCREEN.fill("black")
    pygame.draw.rect(SCREEN, "Blue", rex)
    pygame.draw.rect(SCREEN, "Blue", dex)
    pygame.draw.rect(SCREEN, "Blue", gex)
    SCREEN.lock()
    cir = pygame.draw.circle(SCREEN, (212, 255, 0), cir_rect.size, 20, 0)
    if flag:
        cirl = pygame.draw.circle(SCREEN, (212, 255, 0), cir_rect2.size, 20, 0)
        z=z+1
        if z<800 and z>795:
            c=c-10
    SCREEN.unlock()
    PLAY_TEXT1 = get_font(30).render("THREE processor A->30 B->50 C->10.", True, "White")
    PLAY_RECT1 = PLAY_TEXT1.get_rect(topleft=(0, 0))
    PLAY_TEXT = get_font(45).render("FCFS Scheduling.", True, "White")
    SCREEN.blit(PLAY_TEXT1, PLAY_RECT1)
    PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 60))
    Cir_TEXT = get_font(18).render("20", True, "Red")
    Cir_RECT = Cir_TEXT.get_rect(center=cir_rect.size)
    if flag:
        Cir_TEXT2 = get_font(18).render("30", True, "Red")
        Cir_RECT2 = Cir_TEXT.get_rect(center=cir_rect2.size)
        SCREEN.blit(Cir_TEXT2, Cir_RECT2)
    SCREEN.blit(PLAY_TEXT, PLAY_RECT)
    SCREEN.blit(Cir_TEXT, Cir_RECT)
    x=x+1
    # if flag:
    #     if z>=y:
    #         c=c-1
    cir_rect.update(0,0,x,y)
    cir_rect2.update(0,0,z,c)
    # dis = pygame.draw.circle(SCREEN, (212, 255, 0), (z, y), 20, 0)
    if flag:
        if cirl.colliderect(gex):
            c=c+1
    ans=cir.collidelist(collist)
    if ans== 1:
        y=y+1
        flag=True




    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
            sys.exit()
    pygame.display.update()