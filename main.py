# main.py
# make an original game

# TODO:
#   * Make sprite follow mouse
#   * Change snow to an enemy sprite
#   * Add a background picture
#   * Player collision with enemies

import pygame
import random

# ----- CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
SKY_BLUE = (95, 165, 228)
WIDTH = 1080
HEIGHT = 900
NUM_SNOW = 100
TITLE = "<You're title here>"

# Create snow class based on snowscape project
class Snow:
    def __init__(self, radius=1):
        self.radius = radius

        self.x, self.y = (
            random.randrange(0, WIDTH),
            random.randrange(0, HEIGHT)
        )

        self.colour = WHITE

        self.vel_y = random.choice([1, 2])

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            self.colour,
            (self.x, self.y),
            self.radius
        )

    def update(self):
        self.y += self.vel_y

        if self.y > HEIGHT:
            self.x = random.randrange(0, WIDTH)
            self.y = random.randrange(-15, 0)

# Create  player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./images/rowlet.png")
        self.image = pygame.transform.scale(self.image, (37, 44))
        self.rect = self.image.get_rect()

    def update(self):
        # Changes the position of the player based on the mouse's position
        self.rect.center = pygame.mouse.get_pos()

def main():
    pygame.init()

    # ----- SCREEN PROPERTIES
    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(TITLE)

    # ----- LOCAL VARIABLES
    done = False
    clock = pygame.time.Clock()

    # Sprite group and sprite creation
    all_sprite_group = pygame.sprite.Group()

    # Player creation
    player = Player()
    all_sprite_group.add(player)

    # Create snow objects
    snow_list = []

    # Farther snow
    for i in range(NUM_SNOW):
        snow = Snow()
        snow_list.append(snow)
    for i in range (NUM_SNOW):
        snow = Snow(random.choice([3, 4]))
        snow.vel_y = random.choice([4, 5])
        snow_list.append(snow)

    # ----- MAIN LOOP
    while not done:
        # -- Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ----- LOGIC
        for snow in snow_list:
            snow.update()

        # ----- DRAW
        screen.fill(BLACK)
        for snow in snow_list:
            snow.draw(screen)
        all_sprite_group.draw(screen)

        # ----- UPDATE
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
