import pygame as py
from random import randint
from time import sleep
py.init()
tela = py.display.set_mode((0,0),py.FULLSCREEN)
l,a=tela.get_size()
py.display.set_caption("Coleta Maçã")
rodando = True
vel = 5
vel_x = 0
pontos = 0
player_pos = [700,700]
item_pos = [randint(1,600),10]
while rodando:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
    tela.fill("white")
    texto = py.font.SysFont(None,36).render(str(pontos),True,"black")
    tela.blit(texto,(5,10))
    keys = py.key.get_pressed()
    circulo = py.draw.circle(tela,"black",player_pos,10)
    item = py.draw.circle(tela,"green",item_pos,10)
    if keys[py.K_a] and player_pos[0] > 0:
        vel_x -= vel
    if keys[py.K_d] and player_pos[0] < 601:
        vel_x += vel
    if keys[py.K_LEFT] and player_pos[0] > 0:
        vel_x -= vel
    if keys[py.K_RIGHT] and player_pos[0] < 601:
        vel_x += vel
    player_pos[0] += vel_x
    item_pos[1] += 3
    if circulo.collidepoint(item_pos):
        item_pos[0] = randint(1,600)
        item_pos[1] = 10
        pontos += 1
    if item_pos[1] > 700:
        pontos = "perdeu!, aperte espaço para fechar o jogo"
    vel_x = 0
    if keys[py.K_SPACE]:
        pontos = 'Fechando em 3...'
        texto = py.font.SysFont(None,50).render(str(pontos),True,"black")
        tela.blit(texto,(l//2,a//2))
        py.display.flip()
        sleep(1)
        pontos = 'Fechando em 3... 2...'
        texto = py.font.SysFont(None,50).render(str(pontos),True,"black")
        tela.blit(texto,(l//2,a//2))
        py.display.flip()
        sleep(1)
        pontos = 'Fechando em 3... 2... 1...'
        texto = py.font.SysFont(None,50).render(str(pontos),True,"black")
        tela.blit(texto,(l//2,a//2))
        py.display.flip()
        sleep(1)
        rodando = False
    py.display.flip()
    py.time.Clock().tick(60)