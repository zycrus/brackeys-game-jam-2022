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

# Player Move Function
def PlayerMove(x, y, vel):
    print(player.x)
    keys = pygame.key.get_pressed()
    if (keys[ord('a')]):
        x -= vel
    if (keys[ord('d')]):
        x += vel
    if (keys[ord('w')]):
        y -= vel
    if (keys[ord('s')]):
        y += vel
    UpdatePlayer(x, y)

# Update Player
def UpdatePlayer(x, y):
    player.x = x
    player.y = y
    player.params = (player.x, player.y, player.WIDTH, player.HEIGHT)

# While the Game is Running
run = True
while run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Move Player
    PlayerMove(player.x, player.y, player.vel)
            
    win.fill((0, 0, 0))
    pygame.draw.rect(win, player.color, player.params)
    pygame.display.update()

pygame.quit() # Quit