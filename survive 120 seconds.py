import pygame
import random

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Enemys and Player")

running = True
clock = pygame.time.Clock()

# Colors
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
BLUE = (0, 0, 255)
CYAN = (0, 255, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (150, 150, 150)

# Enemy 1
enemy_y = 50
enemy_x = 50
enemy_speed = 4
enemy_size = 50

# Enemy 2
enemy2_x = 200
enemy2_y = 50
enemy2_bottom = False
enemy2_top = True
enemy2_speed = 10
enemy2_height = 75
enemy2_width = 25

# Enemy 3
enemy3_x = 725
enemy3_y = 950
enemy3_top = False
enemy3_bottom = True
enemy3_speed = 10
enemy3_height = 75
enemy3_width = 25

# Player
player_y = 475
player_x = 475
player_size = 25
speed = 8
lifes = 3

# Bullets
bullet_x, bullet_y = 0, 0
enemy_bullet_speed = 10
bullet_active = False
bullet_width = 15
bullet_height = 15

bullet2_x, bullet2_y = 0, 0
enemy_bullet2_speed = 10
bullet2_active = False
bullet2_width = 15
bullet2_height = 15

time = 30
level = 1
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

    keys = pygame.key.get_pressed()

    """
    ================================
    Player movements and boundaries
    ================================
    """
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        player_y -= speed
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        player_y += speed
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player_x -= speed
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player_x += speed

    if player_x < 0:
        player_x = 0
    if player_x > SCREEN_WIDTH - player_size:
        player_x = SCREEN_WIDTH - player_size
    if player_y < 0:
        player_y = 0
    if player_y > SCREEN_HEIGHT - player_size:
        player_y = SCREEN_HEIGHT - player_size

    """
    ================================
    Enemy projectiles logic
    ================================
    """
    if not bullet_active and bullet_height > 0 and bullet_width > 0:
        bullet_x = enemy2_x 
        bullet_y = enemy2_y
        bullet_active = True

    if bullet_active:
        bullet_x += enemy_bullet_speed 
        if bullet_x >= SCREEN_WIDTH or bullet_y >= SCREEN_HEIGHT or bullet_y <= 0 or bullet_x <= 0:                      
            bullet_active = False
            if level == 5:
                bullet_height = 50

    if not bullet2_active and bullet2_height > 0 and bullet2_width > 0:
        bullet2_x = enemy3_x 
        bullet2_y = enemy3_y
        bullet2_active = True
    
    if bullet2_active:
        bullet2_x -= enemy_bullet2_speed 
        if bullet2_x >= SCREEN_WIDTH or bullet2_y >= SCREEN_HEIGHT or bullet2_y <= 0 or bullet2_x <= 0:                      
            bullet2_active = False
            if level == 5:
                bullet2_height = 50

    if level == 5 and bullet_active: 
        bullet_height += 2

            

    if level == 5 and bullet2_active: 
        bullet2_height += 2
        

    """
    ================================
    Creating the hitboxes safely
    ================================
    """
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_size, enemy_size)
    enemy2_rect = pygame.Rect(enemy2_x, enemy2_y, enemy2_width, enemy2_height)
    enemy3_rect = pygame.Rect(enemy3_x, enemy3_y, enemy3_width, enemy3_height)

    # Use off-screen rects if bullets are inactive to prevent ghost collisions
    if bullet_active:
        bullet_rect = pygame.Rect(bullet_x, bullet_y, bullet_width, bullet_height)
    else:
        bullet_rect = pygame.Rect(-100, -100, 0, 0) 

    if bullet2_active:
        bullet_rect2 = pygame.Rect(bullet2_x, bullet2_y, bullet2_width, bullet2_height)
    else:
        bullet_rect2 = pygame.Rect(-100, -100, 0, 0) 

    """
    ================================
    Collisions
    ================================
    """
    hit = False

    if bullet_active and bullet_rect.colliderect(player_rect): 
        hit = True

    if bullet2_active and bullet_rect2.colliderect(player_rect): 
        hit = True

    if player_rect.colliderect(enemy_rect) or player_rect.colliderect(enemy2_rect) or (enemy3_width > 0 and player_rect.colliderect(enemy3_rect)): 
        hit = True

    if hit:
        lifes -= 1
        if lifes <= 0:
            running = False
        else:
            if level == 1:
                enemy_x = 50
                enemy_y = 50
                player_x = 475
                player_y = 475
                bullet_active = False
                bullet2_active = False

            elif level == 2:
                enemy_x = 50
                enemy_y = 50
                player_x = 950
                player_y = 900

            elif level == 3:
                enemy_x = 50
                enemy_y = 50
                enemy2_y = 0
                enemy3_y = 950
                player_x = 50
                player_y = 900

            elif level == 4:
                enemy_x = 50
                enemy_y = 50
                enemy2_y = 0
                enemy3_y = 600
                player_x = 450
                player_y = 850
                bullet_active = False
                bullet2_active = False

            elif level == 5:
                enemy_x = 50
                enemy_y = 50
                player_x = 850
                player_y = 850
                enemy2_y = 925
                enemy3_y = 25
                bullet_active = False
                bullet2_active = False
                
    

    """
    ================================
    Enemy movements
    ================================
    """
    if enemy_x < player_x:
        enemy_x += enemy_speed
    elif enemy_x > player_x:
        enemy_x -= enemy_speed

    if enemy_y < player_y:
        enemy_y += enemy_speed
    elif enemy_y > player_y:
        enemy_y -= enemy_speed
    
    # Enemy 2 movement
    if not enemy2_bottom:
        enemy2_y += enemy2_speed
        if enemy2_y >= SCREEN_HEIGHT - enemy2_height: 
            enemy2_top = False
            enemy2_bottom = True

    if not enemy2_top:
        enemy2_y -= enemy2_speed
        if enemy2_y <= 0: 
            enemy2_bottom = False
            enemy2_top = True

    # Enemy 3 movement
    if not enemy3_bottom:
        enemy3_y += enemy3_speed
        if enemy3_y >= SCREEN_HEIGHT - enemy3_height: 
            enemy3_top = False
            enemy3_bottom = True
    
    if not enemy3_top:
        enemy3_y -= enemy3_speed
        if enemy3_y <= 0: 
            enemy3_bottom = False
            enemy3_top = True

    """
    ================================
    Level Transition (Time Expired)
    ================================
    """
    if time <= 0 and level == 1:
        time = 30
        level += 1
        enemy_x = 50
        enemy_y = 50
        enemy_size = 50

        enemy2_x = 150
        enemy2_y = 150
        enemy2_height = 250
        enemy2_width = 250
        enemy2_speed = 8
      
        enemy3_height = 250
        enemy3_width = 250
        enemy3_x = 550 
        enemy3_y = 550 
        enemy3_speed = 8

        bullet_width = 0
        bullet_height = 0
        bullet2_height = 0
        bullet2_width = 0
        bullet_active = False
        bullet2_active = False

        player_x = 950
        player_y = 800

        lifes += 1
        

    if time <= 0 and level == 2:
        time = 30
        level += 1
        enemy_x = 50
        enemy_y = 50
        enemy_size = 50

        enemy2_x = 0
        enemy2_y = 50
        enemy2_height = 50
        enemy2_width = 500
        enemy2_speed = 4
        
        enemy3_height = 50
        enemy3_width = 500
        enemy3_x = 500 
        enemy3_y = 950 
        enemy3_speed = 4

        bullet_size = 0
        bullet2_size = 0
        bullet_active = False
        bullet2_active = False

        player_x = 100
        player_y = 800

        lifes += 1

    if time <= 15 and level == 3:
        enemy2_speed = 8
        enemy3_speed = 8
        enemy2_height = 75
        enemy3_height = 75

    if time <= 0 and level == 3:
        time = 30
        enemy_x = 50
        enemy_y = 50
        enemy_size = 50

        enemy2_x = 100
        enemy2_y = 50
        enemy2_height = 150
        enemy2_width = 25
        enemy2_speed = 6
        
        enemy3_height = 150
        enemy3_width = 25
        enemy3_x = 850 
        enemy3_y = 600 
        enemy3_speed = 6

        bullet_width = 20
        bullet_height = 150
        bullet2_height = 150
        bullet2_width = 20
        bullet_active = True
        bullet2_active = True
        enemy_bullet_speed = 4
        enemy_bullet2_speed = 4

        player_x = 450
        player_y = 800

        lifes += 1

    if level == 4 and time <= 15:
        bullet2_height += 0.5
        bullet_height += 0.5
        enemy2_height += 0.5
        enemy3_height += 0.5

    if time <= 0 and level == 4:
        time = 30
        level += 1
        enemy_x = 50
        enemy_y = 50
        enemy_size = 50

        enemy2_x = 25
        enemy2_y = 925
        enemy2_height = 75
        enemy2_width = 75
        enemy2_speed = 4
        
        enemy3_height = 75
        enemy3_width = 75
        enemy3_x = 900
        enemy3_y = 25 
        enemy3_speed = 4

        bullet_width = 20
        bullet_height = 20
        bullet2_height = 50
        bullet2_width = 20
        bullet_active = True
        bullet2_active = True
        enemy_bullet_speed = 8
        enemy_bullet2_speed = 8

        player_x = 450
        player_y = 800

        lifes += 1

        


    """
    ================================
    Drawing Elements
    ================================
    """
    screen.fill(GREY) 

    # Draw Bullets
    if bullet_active:
        pygame.draw.rect(screen, RED, bullet_rect)
    if bullet2_active:
        pygame.draw.rect(screen, RED, bullet_rect2)

    # Draw Enemies and Player
    pygame.draw.rect(screen, RED, enemy_rect)
    pygame.draw.rect(screen, GREEN, player_rect)
    pygame.draw.rect(screen, PURPLE, enemy2_rect)
    if enemy3_width > 0:
        pygame.draw.rect(screen, PURPLE, enemy3_rect)

    # UI Display - Lives
    pygame.draw.rect(screen, BLACK, (30, 33, 60, 60))
    pygame.draw.rect(screen, WHITE, (35, 38, 50, 50))
    font = pygame.font.SysFont(None, 48)
    screen.blit(font.render(f"{lifes}", True, BLACK), (50, 50))
    screen.blit(font.render("Lives", True, BLACK), (25, 100))

    # UI Display - Timer
    pygame.draw.rect(screen, BLACK, (443, 33, 90, 60))
    pygame.draw.rect(screen, WHITE, (448, 38, 80, 50))
    font_large = pygame.font.SysFont(None, 55)
    screen.blit(font_large.render(f"{time}", True, BLACK), (455, 50))
    screen.blit(font_large.render("Time", True, BLACK), (435, 100))

    # UI Display - Level
    pygame.draw.rect(screen, BLACK, (925, 33, 60, 60))
    pygame.draw.rect(screen, WHITE, (930, 38, 50, 50))
    screen.blit(font.render(f"{level}", True, BLACK), (945, 50))
    screen.blit(font.render("Level", True, BLACK), (915, 100))

    pygame.display.flip() 
    clock.tick(60)

pygame.quit()