import pygame
import math
pygame.init()

WIDTH, HEIGHT = 700, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sistema solar")

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (100, 149, 237)
RED = (188, 39, 50)
DARK_GREY = (80, 78, 81)


laser = pygame.mixer.Sound('laser1.wav')

class Player():
    def __init__(self,x,y,mouse_x,mouse_y):
        self.x = x
        self.y = y
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y

       
    def draw(self):
        self.angle = math.degrees(math.atan2(-(self.mouse_y - self.y), self.mouse_x - self.x)) - 90
        self.nave = pygame.image.load("ship1.png").convert_alpha()
        self.nave_r = pygame.transform.rotate(self.nave,self.angle)
        # self.nave_r = pygame.transform.scale(self.nave_r,(120,120))
    
        
        self.nave_rect = pygame.Surface.get_rect(self.nave_r)
        self.nave_rect.center = (WIDTH/2, HEIGHT/2)

        WIN.blit(self.nave_r, self.nave_rect)





class Bullet():
    def __init__(self, x, y, mouse_x, mouse_y):
        self.x = x 
        self.y = y 
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y
        self.lifetime = 50
        self.speed = 10
        self.angle = math.atan2(self.mouse_y - self.y, self.mouse_x - self.x)

        self.angle2 = math.degrees(math.atan2(-(self.mouse_y - self.y), self.mouse_x - self.x)) - 90

        self.x_vel = math.cos(self.angle) * self.speed
        self.y_vel = math.sin(self.angle) * self.speed

        self.tiro = pygame.image.load("new_bullet.png").convert_alpha()
        self.tiro_r = pygame.transform.rotate(self.tiro,self.angle2)
        self.tiro_rect = self.tiro.get_rect(center = (self.x ,self.y ))

        

    def draw(self, display):
        self.tiro_rect.x += int(self.x_vel)
        self.tiro_rect.y += int(self.y_vel)
        display.blit(self.tiro_r, self.tiro_rect)
        self.lifetime -= 1


bullets = []

def main():
    run = True
    clock = pygame.time.Clock()
   
    
   
  
    while run:

        clock.tick(60)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        WIN.fill((255, 255, 255))
        nave = Player(WIDTH/2,HEIGHT/2,mouse_x,mouse_y)
        nave.draw()
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                bullets.append(Bullet(WIDTH/2,HEIGHT/2,mouse_x,mouse_y))
                laser.play()

                
        
        for i in bullets:
            if i.lifetime <= 0:
                bullets.pop(bullets.index(i))
            i.draw(WIN)
        
        pygame.display.update()

    pygame.quit()


main()
