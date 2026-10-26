import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Four Red Squares")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    RED = (255, 0, 0)
    WHITE = (255, 255, 255)

    pygame.draw.rect(screen, RED, (750, 0, 50, 800))
    pygame.draw.rect(screen, RED, (0, 550, 800, 50))
    pygame.draw.rect(screen, RED, (0, 0, 50, 800))
    pygame.draw.rect(screen, RED, (0, 0, 800, 50))

    pygame.draw.rect(screen, WHITE, (120, 100, 10, 100))
    pygame.draw.rect(screen, WHITE, (100, 100, 50, 10))

    pygame.draw.rect(screen, WHITE, (175, 100, 10, 100))
    pygame.draw.rect(screen, WHITE, (175, 100, 50, 10))

    pygame.draw.rect(screen, WHITE, (250, 100, 10, 100))

    pygame.draw.rect(screen, WHITE, (300, 100, 10, 100))
    pygame.draw.rect(screen, WHITE, (300, 100, 50, 10))
    pygame.draw.rect(screen, WHITE, (300, 150, 50, 10))
    pygame.draw.rect(screen, WHITE, (350, 100, 10, 60))

    pygame.draw.rect(screen, WHITE, (400, 100, 10, 100))
    pygame.draw.rect(screen, WHITE, (400, 100, 50, 10))
    pygame.draw.rect(screen, WHITE, (400, 150, 50, 10))
    pygame.draw.rect(screen, WHITE, (450, 100, 10, 60))

    pygame.draw.rect(screen, WHITE, (500, 100, 10, 100))

    pygame.draw.rect(screen, WHITE, (550, 100, 10, 100))
    pygame.draw.rect(screen, WHITE, (550, 100, 50, 10))
    pygame.draw.rect(screen, WHITE, (550, 150, 50, 10))
    pygame.draw.rect(screen, WHITE, (550, 200, 50, 10))

    pygame.draw.rect(screen, WHITE, (100, 250, 10, 100))
    pygame.draw.rect(screen, WHITE, (100, 250, 50, 10))

    pygame.draw.rect(screen, WHITE, (175, 250, 10, 100))
    pygame.draw.rect(screen, WHITE, (175, 250, 50, 10))
    pygame.draw.rect(screen, WHITE, (175, 300, 50, 10))
    pygame.draw.rect(screen, WHITE, (175, 350, 50, 10))

    pygame.draw.rect(screen, WHITE, (250, 250, 10, 100))
    pygame.draw.rect(screen, WHITE, (300, 260, 10, 90))
    pygame.draw.rect(screen, WHITE, (250, 250, 50, 10))
    pygame.draw.rect(screen, WHITE, (250, 350, 50, 10))
    
    pygame.draw.rect(screen, WHITE, (325, 250, 10, 100))
    pygame.draw.rect(screen, WHITE, (375, 260, 10, 90))
    pygame.draw.rect(screen, WHITE, (325, 250, 50, 10))
    pygame.draw.rect(screen, WHITE, (325, 350, 50, 10))
    
    
    

    


    pygame.display.flip() 

pygame.quit()