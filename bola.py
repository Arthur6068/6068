import pygame
pygame.init()
tela=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
l,a=tela.get_size()
b=(255,255,255)
while True:
    for ev in pygame.event.get():
        if ev.type==pygame.MOUSEMOTION:
            pos=pygame.mouse.get_pos()
            cor=(0,255,255)
            pygame.draw.circle(tela,cor,pos,20,5)
        fonte = pygame.font.Font(None, 50)
        mensagem = fonte.render('aperte espaço para fechar', True, 'white')
        retangulo_mensagem = mensagem.get_rect(center=(l//2,a//2))
        tela.blit(mensagem, retangulo_mensagem)
        t=pygame.key.get_pressed()    
        if t[pygame.K_SPACE]:
            pygame.quit()
        if ev.type==pygame.QUIT:
            pygame.quit()
    pygame.display.update()