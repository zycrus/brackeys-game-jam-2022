import pygame

# Initialize Pygame
pygame.init()

# Initialize Pygame Window/Display
class Window():
    def __init__(self, WIDTH, HEIGHT):
        self.x = 0
        self.WIDTH = WIDTH # Width
        self.y = 0
        self.HEIGHT = HEIGHT # Height

win_instance = Window(750, 500)

win = pygame.display.set_mode((win_instance.WIDTH, win_instance.HEIGHT))
pygame.display.set_caption("wow")


# Player Class
class Player():

    def __init__(self, x, y):
        self.x = 250 # Horizontal Position
        self.y = 250 # Vertical Position
        self.WIDTH = 50 # Width
        self.HEIGHT = 50 # Height
        self.params = (self.x, self.y, self.WIDTH, self.HEIGHT) # Parameters
        self.color = (255, 0, 0) # Player Color
        self.vel = 5 # PLayer Speed
        self.isGrounded = False
        self.jumpSpeed = 2
        self.currentJumpSpeed = 2
        self.jumpMax = 32


# Initialize Player Object named player
player = Player(250, 250)

# Ground Class
class Ground():

    def __init__(self, x, y, _width, _height):
        self.x = x # Horizontal Position
        self.y = y # Vertical Position
        self.WIDTH = _width # Width
        self.HEIGHT = _height # Height
        self.params = (self.x, self.y, self.WIDTH, self.HEIGHT)
        self.color = (85, 65, 24) # Ground Color

ground = Ground(0, win_instance.HEIGHT - 30, win_instance.WIDTH, 30)

# Player Move Function
def PlayerMove(x, y, vel):
    keys = pygame.key.get_pressed()
    if (keys[ord('a')]) and (PlayerCollideBoundaries(player, win_instance) != "left_collide"):
        x -= vel
    if (keys[ord('d')]) and (PlayerCollideBoundaries(player, win_instance) != "right_collide"):
        x += vel
    #if (keys[ord('w')]) and (PlayerCollideBoundaries(player, win_instance) != "up_collide"):
        #y -= vel
    if (keys[ord('s')]) and (PlayerCollideBoundaries(player, win_instance) != "down_collide"):
        y += vel
    if (keys[pygame.K_SPACE]) and player.isGrounded:
        PlayerJump()
    UpdatePlayer(x, y)


# - - - - Collision - - - - - - - - - 

# Check Player Collision
def CheckPlayerCol(player, other):
    # Check Horizontal Collisions
    if (player.x - player.vel < other.x):
        player.x = other.x
    elif (player.x + player.WIDTH + player.vel > other.WIDTH):
        player.x = other.WIDTH - player.WIDTH
    # Check Vertical Collisions
    if (player.y - player.vel < other.y):
        player.y = other.y
    elif (player.y + player.HEIGHT + player.vel > other.HEIGHT):
        player.y = other.HEIGHT - player.HEIGHT

def PlayerCollideBoundaries(player, other):
    # Check Horizontal Collisions
    if (player.x - player.vel < other.x):
        return "left_collide"
    if (player.x + player.WIDTH + player.vel > other.WIDTH):
        return "right_collide"
    # Check Vertical Collisions
    if (player.y - player.vel < other.y):
        return "up_collide"
    if (player.y + player.HEIGHT + player.vel > other.HEIGHT):
        return "down_collide"

# - - - - - - - - - - - - - - - - - - -




# Gravity
def Gravity():
    fall_spd = 20
    if (player.y + player.HEIGHT - player.vel < ground.y - ground.HEIGHT):
        player.y += fall_spd
        player.isGrounded = False
    else:
        player.isGrounded = True
        fall_spd = 0
        player.y = ground.y - player.HEIGHT

# Jump
def PlayerJump():
    return



# Update Player
def UpdatePlayer(x, y):
    player.x = x
    player.y = y
    player.params = (player.x, player.y, player.WIDTH, player.HEIGHT)
    Gravity()
    CheckPlayerCol(player, win_instance)

# While the Game is Running
run = True
while run:
    pygame.time.delay(20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Move Player
    PlayerMove(player.x, player.y, player.vel)
    print(player.isGrounded)
            
    win.fill((0, 0, 0))
    pygame.draw.rect(win, player.color, player.params)
    pygame.draw.rect(win, ground.color, ground.params)
    pygame.display.update()

pygame.quit() # Quit