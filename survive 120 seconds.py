import pygame

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Enemys and Player")

running = True

clock = pygame.time.Clock()

RED = (255, 0, 0)
PURPLE = (255, 0, 255)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0) 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (150, 150, 150)

enemy_y = 50
enemy_x = 50
enemy_speed = 4

enemy2_x = 200
enemy2_y = 50
enemy2_bottom = False
enemy2_top = True
enemy2_speed = 10

enemy3_x = 725
enemy3_y = 950
enemy3_top = False
enemy3_bottom = True
enemy3_speed = 10

player_y = 475
player_x = 475
player_size = 25
speed = 8
lifes = 3

enemy_bullet_speed = 10
bullet_active = False

enemy_bullet2_speed = 10
bullet2_active = False

time = 120
win = False

COUNTDOWN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(COUNTDOWN_EVENT, 1000)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == COUNTDOWN_EVENT:
            if time > 0:
                time -= 1
               
            elif time <= 0:
                win = True
            if win == True:
                font = pygame.font.SysFont(None, 48)
                message = font.render("YOU WIN!", True, BLACK)
                screen.blit(message, (425, 180))
                speed = 0
                enemy_speed = 0
                enemy2_speed = 0
                enemy3_speed = 0

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        player_y = player_y - speed

    if keys[pygame.K_s]:
        player_y = player_y + speed

    if keys[pygame.K_a]:
        player_x = player_x - speed

    if keys[pygame.K_d]:
        player_x = player_x + speed

    if player_x < 0:
        player_x = 0

    if player_x > SCREEN_WIDTH - player_size:
        player_x = SCREEN_WIDTH - player_size

    if player_y < 0:
        player_y = 0

    if player_y > SCREEN_HEIGHT - player_size:
        player_y = SCREEN_HEIGHT - player_size

    if not bullet_active:
        bullet_x = enemy2_x 
        bullet_y = enemy2_y
        bullet_active = True

    if bullet_active:
            bullet_x += enemy_bullet_speed 

            if bullet_x >= 1000 or bullet_y >= 1000 or bullet_y <= 0 or bullet_x <= 0:                      
                bullet_active = False

    if not bullet2_active:
            bullet2_x = enemy3_x 
            bullet2_y = enemy3_y
            bullet2_active = True
    
    if bullet2_active:
            bullet2_x -= enemy_bullet_speed 

            if bullet2_x >= 1000 or bullet2_y >= 1000 or bullet2_y <= 0 or bullet2_x <= 0:                      
                bullet2_active = False

    if bullet_active:
        pygame.draw.rect(screen, RED, (bullet_x, bullet_y, 15, 15))

    if bullet2_active:
        pygame.draw.rect(screen, RED, (bullet2_x, bullet2_y, 15, 15))

    player_rect = pygame.Rect(player_x, player_y, 25, 25)

    enemy_rect = pygame.Rect(enemy_x, enemy_y, 50, 50)
    enemy2_rect = pygame.Rect(enemy2_x, enemy2_y, 25, 75)
    enemy3_rect = pygame.Rect(enemy3_x, enemy3_y, 25, 75)

    bullet_rect = pygame.Rect(bullet_x,bullet_y,15,15)
    bullet_rect2 = pygame.Rect(bullet2_x,bullet2_y,15,15)

    if bullet_rect.colliderect(player_rect):
        lifes -= 1
        if lifes == 0:
            running = False
        else:
            enemy_x = 50
            enemy_y = 50
            player_x = 475
            player_y = 475
            bullet_active = False
            bullet2_active = False

    if bullet_rect2.colliderect(player_rect):
        lifes -= 1
        if lifes == 0:
            running = False
        else:
            enemy_x = 50
            enemy_y = 50
            player_x = 475
            player_y = 475
            bullet2_active = False
            bullet_active = False

    if player_rect.colliderect(enemy_rect) or player_rect.colliderect(enemy2_rect) or player_rect.colliderect(enemy3_rect):
        lifes -= 1
        if lifes == 0:
            running = False
        else:
            enemy_x = 50
            enemy_y = 50
            player_x = 475
            player_y = 475
            bullet2_active = False
            bullet_active = False


    if enemy_x < player_x:
        enemy_x += enemy_speed
    elif enemy_x > player_x:
        enemy_x -= enemy_speed
    if enemy_y < player_y:
        enemy_y += enemy_speed
    elif enemy_y > player_y:
        enemy_y -= enemy_speed
    
    if enemy2_bottom == False:
        enemy2_y += enemy2_speed
        if enemy2_y == 1000:
            enemy2_top = False
            enemy2_bottom = True

    if enemy2_top == False:
        enemy2_y -= enemy2_speed
        if enemy2_y == 0:
            enemy2_bottom = False
            enemy2_top = True

    if enemy3_bottom == False:
        enemy3_y += enemy3_speed
        if enemy3_y == 1000:
            enemy3_top = False
            enemy3_bottom = True
    
    if enemy3_top == False:
        enemy3_y -= enemy3_speed
        if enemy3_y == 0:
            enemy3_bottom = False
            enemy3_top = True

    pygame.draw.rect(screen, BLACK, (30, 33, 60, 60))
    pygame.draw.rect(screen, WHITE, (35, 38, 50, 50))

    font = pygame.font.SysFont(None, 48)
    message = font.render(f"{lifes}", True, BLACK)
    screen.blit(message, (50, 50))

    pygame.draw.rect(screen, BLACK, (443, 33, 90, 60))
    pygame.draw.rect(screen, WHITE, (448, 38, 80, 50))
    
    font = pygame.font.SysFont(None, 55)
    message = font.render(f"{time}", True, BLACK)
    screen.blit(message, (455, 50))

    pygame.draw.rect(screen, RED, (enemy_x, enemy_y, 50, 50))
    pygame.draw.rect(screen, GREEN, (player_x, player_y, player_size, player_size))
    pygame.draw.rect(screen, PURPLE, (enemy2_x, enemy2_y, 25, 75))
    pygame.draw.rect(screen, PURPLE, (enemy3_x, enemy3_y, 25, 75))

    pygame.display.flip() 

    clock.tick(60)

    screen.fill(GREY)

pygame.quit()