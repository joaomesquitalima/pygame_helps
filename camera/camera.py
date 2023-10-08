import pygame

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("My Simple Game")

clock = pygame.time.Clock()

BACKGROUND_COLOR = (255, 255, 255)

PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50

player_x = WINDOW_WIDTH // 2 
player_y = WINDOW_HEIGHT //2

PLAYER_SPEED = 10

RECTANGLE_COLOR_1 = (255, 0, 0)
RECTANGLE_COLOR_2 = (0, 0, 255)

rectangle_1 = pygame.Rect(200, 200, 100, 100)
rectangle_2 = pygame.Rect(500, 300, 150, 50)

# inica o joystick
pygame.joystick.init()
joysticks = []  # recebe comandos do joystick
# Set the camera offset
camera_offset_x = 0
camera_offset_y = 0
while True:
    for joystick in joysticks:
            # analogico esquerdo
            horiz_move = joystick.get_axis(0)
            vert_move = joystick.get_axis(1)
            camera_offset_x -= horiz_move*-5
            camera_offset_y -= vert_move*-5

            

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.JOYDEVICEADDED:
                joy = pygame.joystick.Joystick(event.device_index)
                joysticks.append(joy)

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                camera_offset_x -= PLAYER_SPEED
            elif event.key == pygame.K_RIGHT:
                camera_offset_x += PLAYER_SPEED
            
            if event.key == pygame.K_UP:
                camera_offset_y -= PLAYER_SPEED
            elif event.key == pygame.K_DOWN:
                camera_offset_y += PLAYER_SPEED

    # Draw the background
    screen.fill(BACKGROUND_COLOR)

    # Draw the static rectangles
    rectangle_1_draw_pos = rectangle_1.move(camera_offset_x, camera_offset_y)
    pygame.draw.rect(screen, RECTANGLE_COLOR_1, rectangle_1_draw_pos)
        
    rectangle_2_draw_pos = rectangle_2.move(camera_offset_x, camera_offset_y)
    pygame.draw.rect(screen, RECTANGLE_COLOR_2, rectangle_2_draw_pos)
    # Draw the player
    player_rect = pygame.Rect(player_x+ 0, player_y, PLAYER_WIDTH,PLAYER_HEIGHT)

    pygame.draw.rect(screen, (0, 0, 0), player_rect)

    # Update the display
    pygame.display.update()

    # Limit the frame rate
    clock.tick(30)