
import random
import pygame

start_time = pygame.time.get_ticks()
pygame.init()
screen_width = 2000

screen_height = 1000


def check_color_collision(self):
    WHITE = (255, 255, 255)
    # Check if the sprite is touching a certain color (e.g., WHITE) on the screen
    for x in range(self.rect.left, self.rect.right):
        for y in range(self.rect.top, self.rect.bottom):
            if screen.get_at((x, y)) == WHITE:
                return True  # The sprite is touching white
    return False  # The sprite is not touching white

screen = pygame.display.set_mode((screen_width, screen_height))
player = pygame.Rect((300, 250, 50, 50))
dot = pygame.Rect((300, 100, 50, 50))
white = (255, 255, 255)
def jump():
    for i in range(3):
        player.move_ip(0, -2)
lives = 5
run = True
while run:
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), player)
    pygame.draw.rect(screen, (255, 255, 255), dot)
    current = pygame.time.get_ticks()
    key = pygame.key.get_pressed()
    player_x = player.x
    player_y = player.y
    if key[pygame.K_a] == True and player_x >= -5:
        player.move_ip(-2, 0)
    if key[pygame.K_d] == True and player_x <= 1950:
        player.move_ip(2, 0)
    if key[pygame.K_w] == True and player_y >= -3 and current - start_time >= 1000:
        jump()
    if dot.x < player_x:
        dot.move_ip(1, 0)
    elif dot.x > player_x:
        dot.move_ip(-1, 0)
    if dot.y < player_y:
        dot.move_ip(0, 1)
    elif dot.y > player_y:
        dot.move_ip(0, -1)

        pygame.draw.rect(screen, (255, 255, 0), player)
    # if check_color_collision(player):
    #     lives -= 1
    #     pygame.draw.rect(screen, (255, 255, 0), player)



    if player_y <= 950:
        player.move_ip(0, 2)






    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False



    pygame.display.update()
pygame.quit()
