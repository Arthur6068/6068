import pygame as py
py.init()
tela = py.display.set_mode((700,500))
clicando = 0
pontos = 0
click = 1
space = 0
rodando=True
py.display.set_caption('Clicker')
font = py.font.SysFont(None,36)
while rodando:
    for event in py.event.get():
        if event.type == py.QUIT:
            rodando=False
    tela.fill("black")
    keys = py.key.get_pressed()
    retangulo = py.draw.rect(tela,"green",py.Rect(250,200,200,100))
    if event.type == py.MOUSEBUTTONDOWN:
        if retangulo.collidepoint(event.pos) and clicando == 0:
            pontos += click
            clicando = 1
    elif event.type == py.MOUSEBUTTONUP:
        clicando = 0
    if keys[py.K_SPACE] and space == 0 and pontos != 0:
        click = pontos
        pontos = 0
        space = 1
    else:
        space = 0
    texto = font.render(f'{pontos}',True,"white")
    tela.blit(texto,(10,10))
    py.display.flip()
    py.time.Clock().tick(0)