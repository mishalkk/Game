import pygame

pygame.init()
win = pygame.display.set_mode((500,500))
pygame.display.set_caption("WIN")

x = 50
y = 50
radius =40
run = True

while run:

    pygame.time.delay(40)

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            run = False

    pygame.draw.circle(win,(255,0,0),(x,y),radius,1)
    pygame.display.update()

pygame.quit()