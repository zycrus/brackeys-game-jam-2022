import pygame

# Initialize Pygame
pygame.init()

# Initialize Pygame Window/Display
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("wow")


# Player Class
class Player():
    x = 250 # Horizontal Position
    y = 250 # Vertical Position
    WIDTH = 50 # Width
    HEIGHT = 60 # Height
    params = (x, y, WIDTH, HEIGHT) # Parameters
    color = (255, 0, 0) # Player Color
    vel = 5 # PLayer Speed


# Initialize Player Object named player
player = Player()

# While the Game is Running
run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    pygame.draw.rect(win, player.color, player.params)
    pygame.display.update()

pygame.quit() # Quit