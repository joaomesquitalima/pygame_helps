import pygame
import math
pygame.init()

WIDTH, HEIGHT = 400, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sistema solar")

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (100, 149, 237)
RED = (188, 39, 50)
DARK_GREY = (80, 78, 81)

nave = pygame.image.load("nave.png").convert_alpha()
x = WIDTH/2
y = HEIGHT/2

nave_r = pygame.transform.rotate(nave,0)

def main():
    run = True
    clock = pygame.time.Clock()


    while run:

        clock.tick(60)

        WIN.fill((255, 255, 255))
        

        pos = pygame.mouse.get_pos()
        x_dist  = pos[0] - x
        y_dist =  -(pos[1] - y)
        angle =  math.degrees(math.atan2(y_dist,x_dist)) -90
        nave_r = pygame.transform.rotate(nave,angle)
        nave_rect = nave_r.get_rect(center = (x,y))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        WIN.blit(nave_r, nave_rect)
        pygame.display.update()

    pygame.quit()


main()
