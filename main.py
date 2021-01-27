# main.py
# make an original game

# TODO:
#   * Spawn multiple enemies
#   * Change controlto WASD
#   * Print score in terminal

import pygame
import random

# ----- CONSTANTS
GREEN = (0, 170, 40)
WIDTH = 600
HEIGHT = 800
MAX_ENEMY = 10
ENEMY_VEL = 20
TITLE = "squish"

# Create player class, scale image
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./images/toad.png")
        self.image = pygame.transform.scale(self.image, (54, 75))
        self.rect = self.image.get_rect()

    def update(self):
        # Changes the position of the player based on the mouse's position
        self.rect.center = pygame.mouse.get_pos()
                
        # Restrict player height
        if self.rect.top < HEIGHT - 75:
            self.rect.top = HEIGHT - 75

# Create enemy class, scale image
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./images/thwomp.png")
        self.image = pygame.transform.scale(self.image, (107, 120))
        self.rect = self.image.get_rect()
    
        self.rect.x = random.randrange(0, WIDTH)
        self.rect.y = random.randrange(-20, 0)
        
        self.vel_y = ENEMY_VEL

    def update(self):
        self.rect.y += self.vel_y
        

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
    enemy_group = pygame.sprite.Group()

    # Player and enemy creation
    player = Player()
    all_sprite_group.add(player)

    # Enemy
    enemy = Enemy()
    all_sprite_group.add(enemy)
    enemy_group.add(enemy)

    # ----- MAIN LOOP
    while not done:
        # -- Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ----- LOGIC
        all_sprite_group.update()

        # Player collides with a jewel
        enemies_hit = pygame.sprite.spritecollide(player, enemy_group, False)
        if len(enemies_hit) > 0:
            player.kill()

        # ----- DRAW
        screen.fill(GREEN)
        all_sprite_group.draw(screen)

        # ----- UPDATE
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()

