import pygame as py
from random import randint
py.init()
py.mixer.music.load('pvz.mp3')
py.mixer.music.play(loops=-1)
l, a = 1300, 700
tela = py.display.set_mode((l, a))
py.display.set_caption('pegue as bolas brancas')
ciano=(0,255,255)
pontos = 0
vel = 5
vel_x = 0
vel_y = 0
raio = 10
player_pos = [300, 150]
item_pos = [randint(1, 1200), randint(1, 600)]
clock = py.time.Clock()
font = py.font.SysFont(None, 36)
while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
    tela.fill("black")
    bola = py.draw.circle(tela, ciano, player_pos, raio)
    item = py.draw.circle(tela, "white", item_pos, 10)
    keys = py.key.get_pressed()
    vel_x = 0
    vel_y = 0
    if keys[py.K_w] and player_pos[1] - raio > 0:
        vel_y -= vel
    if keys[py.K_s] and player_pos[1] + raio < a:
        vel_y += vel
    if keys[py.K_a] and player_pos[0] - raio > 0:
        vel_x -= vel
    if keys[py.K_d] and player_pos[0] + raio < l:
        vel_x += vel
    if keys[py.K_UP] and player_pos[1] - raio > 0:
        vel_y -= vel
    if keys[py.K_DOWN] and player_pos[1] + raio < a:
        vel_y += vel
    if keys[py.K_LEFT] and player_pos[0] - raio > 0:
        vel_x -= vel
    if keys[py.K_RIGHT] and player_pos[0] + raio < l:
        vel_x += vel
    player_pos[0] += vel_x
    player_pos[1] += vel_y
    if bola.collidepoint(item_pos):
        item_pos = [randint(1, 1200), randint(1, 600)]
        pontos += 1
        raio+=1
        vel += 1
    texto = font.render(str(pontos), True, "green")
    tela.blit(texto, (l // 2, a // 2))
#hack pelas linhas abaixo
    #if player_pos!=item_pos:
        #player_pos=item_pos
    py.display.flip()
    clock.tick(30)