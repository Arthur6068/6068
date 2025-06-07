import pygame
import random
# Inicializa o Pygame
pygame.init()

# Configurações da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Desvie dos quadrados azuis')

# Cores
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Configurações do jogador
player_size = 50
player_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT - 2 * player_size]
player_speed = 10

# Configurações dos inimigos
enemy_size = 50
enemy_list = []
enemy_speed = 10

def create_enemy():
    while True:
        enemy_pos = [random.randint(0, SCREEN_WIDTH - enemy_size), 0]
        if all(abs(enemy_pos[0] - e[0]) > enemy_size for e in enemy_list):
            enemy_list.append(enemy_pos)
            break

for _ in range(5):
    create_enemy()

clock = pygame.time.Clock()

game_over = False

# Função para desenhar elementos na tela
def draw_elements():
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (player_pos[0], player_pos[1], player_size, player_size))
    for enemy_pos in enemy_list:
        pygame.draw.rect(screen, BLUE, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))
    pygame.display.update()

# Loop principal do jogo
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_pos[0] < SCREEN_WIDTH - player_size:
        player_pos[0] += player_speed

    for enemy_pos in enemy_list:
        enemy_pos[1] += enemy_speed
        if enemy_pos[1] > SCREEN_HEIGHT:
            enemy_pos[0] = random.randint(0, SCREEN_WIDTH - enemy_size)
            enemy_pos[1] = 0
        if (enemy_pos[0] < player_pos[0] < enemy_pos[0] + enemy_size or
            enemy_pos[0] < player_pos[0] + player_size < enemy_pos[0] + enemy_size) and \
            (enemy_pos[1] < player_pos[1] < enemy_pos[1] + enemy_size or
            enemy_pos[1] < player_pos[1] + player_size < enemy_pos[1] + enemy_size):
                game_over = True
                print("Game Over")

    draw_elements()
    clock.tick(30)

pygame.quit()